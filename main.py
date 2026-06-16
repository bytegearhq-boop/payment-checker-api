import importlib.util
import os
import sys
import json
import asyncio
from fastapi import FastAPI, Query, HTTPException
from concurrent.futures import ThreadPoolExecutor

app = FastAPI(title="Payment Checker API")

# Load mapping
with open("mapping.json", "r") as f:
    MAPPING = json.load(f)

CHECKERS_DIR = "checkers"
executor = ThreadPoolExecutor(max_workers=20)  # Allow up to 20 concurrent checks

def get_checker_module(checker_name):
    if checker_name not in MAPPING:
        return None
    
    filename = MAPPING[checker_name]
    file_path = os.path.join(CHECKERS_DIR, filename)
    
    if not os.path.exists(file_path):
        return None
        
    module_name = f"checkers.{checker_name}"
    # Reloading or ensuring module is available
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

def run_checker_sync(checker_name, card_input):
    module = get_checker_module(checker_name)
    if not module:
        return {"status": "Error", "message": "Checker not found"}
    
    try:
        # 1. Special case for avspfw1
        if hasattr(module, 'avspfw1'):
            checker = module.avspfw1()
            result = checker.main(card_input)
            return {"status": result[0], "message": result[1]}

        # 2. Check for 'braintrepay' class
        if hasattr(module, 'braintrepay'):
            checker = module.braintrepay(card_input)
            result = checker.main()
            return {"status": result[0], "message": result[1]}
            
        # 3. Check for other classes
        class_names = ["stripe4", "stripe3", "stripe_auth2", "stripeautmass", "braintree", "braintree_bueno", "braintree_malo", "braintreechegd", "payflowchgr", "payflow_pro", "otropayflow", "paypal1", "avspfw"]
        for attr in dir(module):
            if attr in class_names:
                cls = getattr(module, attr)
                if isinstance(cls, type):
                    checker = cls(card_input)
                    result = checker.main()
                    return {"status": result[0], "message": result[1]}

        # 4. Check for 'autnet_woo' class
        if hasattr(module, 'autnet_woo'):
            checker = module.autnet_woo()
            result = checker.main(card_input)
            if isinstance(result, tuple):
                return {"status": result[0], "message": result[1]}
            return {"result": result}

        # 5. Generic main function (sync)
        if hasattr(module, 'main') and not asyncio.iscoroutinefunction(module.main):
            result = module.main(card_input)
            if isinstance(result, tuple):
                return {"status": result[0], "message": result[1]}
            return {"result": result}

        return None # Indicate it might be async
        
    except Exception as e:
        error_msg = getattr(e, 'message', repr(e))
        return {"status": "Error", "message": error_msg}

@app.get("/api/{checker_name}")
async def check_card(checker_name: str, card_input: str = Query(..., alias="str", description="Card string in CC|MM|YY|CVV format")):
    # Check if it's a known async checker first
    module = get_checker_module(checker_name)
    if not module:
        raise HTTPException(status_code=404, detail="Checker not found")

    # Handle async process_zippkits specifically
    if hasattr(module, 'process_zippkits'):
        cc_parts = card_input.split('|')
        if len(cc_parts) < 4:
            raise HTTPException(status_code=400, detail="Invalid card format")
        status, msg = await module.process_zippkits(cc_parts[0], cc_parts[1], cc_parts[2], cc_parts[3])
        return {"status": status, "message": msg}
    
    # Handle other async main functions
    if hasattr(module, 'main') and asyncio.iscoroutinefunction(module.main):
        result = await module.main(card_input)
        if isinstance(result, tuple):
            return {"status": result[0], "message": result[1]}
        return {"result": result}

    # For all other synchronous scripts, run them in a separate thread to avoid blocking
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(executor, run_checker_sync, checker_name, card_input)
    
    if result is None:
        raise HTTPException(status_code=500, detail="No valid entry point found in script")
        
    return result

@app.get("/")
async def root():
    return {"message": "Payment Checker API is running", "endpoints": list(MAPPING.keys())}
