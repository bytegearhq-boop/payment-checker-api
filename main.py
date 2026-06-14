import importlib.util
import os
import sys
import json
import asyncio
from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Payment Checker API")

# Load mapping
with open("mapping.json", "r") as f:
    MAPPING = json.load(f)

CHECKERS_DIR = "checkers"

def get_checker_module(checker_name):
    if checker_name not in MAPPING:
        return None
    
    filename = MAPPING[checker_name]
    file_path = os.path.join(CHECKERS_DIR, filename)
    
    if not os.path.exists(file_path):
        return None
        
    module_name = f"checkers.{checker_name}"
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

@app.get("/api/{checker_name}")
async def check_card(checker_name: str, str: str = Query(..., description="Card string in CC|MM|YY|CVV format")):
    module = get_checker_module(checker_name)
    if not module:
        raise HTTPException(status_code=404, detail="Checker not found")
    
    try:
        # Different scripts have different entry points. We need to handle them.
        # 1. Check for 'braintrepay' class (common in these scripts)
        if hasattr(module, 'braintrepay'):
            checker = module.braintrepay(str)
            result = checker.main()
            return {"status": result[0], "message": result[1]}
            
        # 2. Check for 'stripe4' class (or similar named classes)
        for attr in dir(module):
            if attr in ["stripe4", "stripe3", "stripe_auth2", "stripeautmass", "braintree", "braintree_bueno", "braintree_malo", "braintreechegd"]:
                cls = getattr(module, attr)
                if isinstance(cls, type):
                    checker = cls(str)
                    result = checker.main()
                    return {"status": result[0], "message": result[1]}

        # 3. Check for 'autnet_woo' class
        if hasattr(module, 'autnet_woo'):
            checker = module.autnet_woo()
            result = checker.main(str)
            # Handle different return types
            if isinstance(result, tuple):
                return {"status": result[0], "message": result[1]}
            return {"result": result}

        # 4. Check for async 'process_zippkits' (or similar async functions)
        if hasattr(module, 'process_zippkits'):
            cc_parts = str.split('|')
            if len(cc_parts) < 4:
                raise HTTPException(status_code=400, detail="Invalid card format. Need CC|MM|YY|CVV")
            status, msg = await module.process_zippkits(cc_parts[0], cc_parts[1], cc_parts[2], cc_parts[3])
            return {"status": status, "message": msg}

        # 5. Generic main function
        if hasattr(module, 'main'):
            if asyncio.iscoroutinefunction(module.main):
                result = await module.main(str)
            else:
                result = module.main(str)
            
            if isinstance(result, tuple):
                return {"status": result[0], "message": result[1]}
            return {"result": result}

        raise HTTPException(status_code=500, detail="No valid entry point found in script")
        
    except Exception as e:
        return {"status": "Error", "message": str(e)}

@app.get("/")
async def root():
    return {"message": "Payment Checker API is running", "endpoints": list(MAPPING.keys())}
