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
    res = requests.post("https://api.capsolver.com/createTask", json=payload)
    resp = res.json()
    task_id = resp.get("taskId")
    if not task_id:
        print("Failed to create task:", res.text)
        return

    while True:
        time.sleep(3)  # delay
        payload = {"clientKey": api_key, "taskId": task_id}
        res = requests.post("https://api.capsolver.com/getTaskResult", json=payload)
        resp = res.json()
        status = resp.get("status")
        if status == "ready":
            return resp.get("solution", {}).get('gRecaptchaResponse')
        if status == "failed" or resp.get("errorId"):
            return
Agent = UserAgent().random
def generar_codigo_session():
    codigo_session = str(uuid.uuid4())
    return codigo_session
session = requests.session()
CorreoRand = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com"
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'es-ES,es;q=0.5',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.anfittingsdirect.com/stainless-steel-lines/',
    'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Brave";v="146"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
    # 'cookie': 'cookie_test=please_accept_for_session; osCsid=4051906790886dd6f332098f68f881eb',
}

response = session.get(
    'https://www.anfittingsdirect.com/an-fittings/water-to-air-fittings-p-992.html',

    headers=headers,
)
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'es-ES,es;q=0.5',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.anfittingsdirect.com',
    'priority': 'u=0, i',
    'referer': 'https://www.anfittingsdirect.com/an-fittings/water-to-air-fittings-p-992.html',
    'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Brave";v="146"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
    # 'cookie': 'cookie_test=please_accept_for_session; osCsid=4051906790886dd6f332098f68f881eb',
}

params = {
    'action': 'add_product',
}

data = {
    'products_id': '992',
    'cart_quantity': '1',
}

response = session.post(
    'https://www.anfittingsdirect.com/shopping_cart.php',
    params=params,
    headers=headers,
    data=data,
).text
"""tokens = re.findall(r"authorization:\s*'([^']+)'", response)"""

match = re.search(r"authorization:\s*'([^']+)'", response)
token = match.group(1)
decode = base64.b64decode(token)
decode_string = decode.decode("utf-8")

json_data = json.loads(decode_string)   

bearer = json_data.get('authorizationFingerprint')
print(bearer)

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'es-ES,es;q=0.5',
    'priority': 'u=0, i',
    'referer': 'https://www.anfittingsdirect.com/shopping_cart.php',
    'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Brave";v="146"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
    # 'cookie': 'cookie_test=please_accept_for_session; osCsid=4051906790886dd6f332098f68f881eb',
}

response = session.get('https://www.anfittingsdirect.com/create_account.php', headers=headers).text

url = 'https://www.anfittingsdirect.com/create_account.php'
key_url = '6Le8uk8UAAAAAKmSdQU9NjX37lzlRdkZVvaa43nY'
tipo = 'ReCaptchaV2TaskProxyLess'

cap = capsolver(key_url, url, tipo)
print(cap)
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'es-ES,es;q=0.5',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.anfittingsdirect.com',
    'priority': 'u=0, i',
    'referer': 'https://www.anfittingsdirect.com/create_account.php',
    'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Brave";v="146"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
    # 'cookie': 'cookie_test=please_accept_for_session; osCsid=4051906790886dd6f332098f68f881eb',
}

data = f'action=process&firstname=ldfl&lastname=dsdasd&street_address=calle3&suburb=sadw&city=Ciudad+de+M%E9xico&state=43&postcode=10080&country=223&telephone=%2B10989861371&email_address={CorreoRand}&password=leito132asd&confirmation=leito132asd&g-recaptcha-response={cap}'

response = session.post('https://www.anfittingsdirect.com/create_account.php', headers=headers, data=data)


headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'es-ES,es;q=0.5',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.anfittingsdirect.com/create_account.php',
    'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Brave";v="146"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
    # 'cookie': 'cookie_test=please_accept_for_session; osCsid=4051906790886dd6f332098f68f881eb',
}

response = session.get('https://www.anfittingsdirect.com/checkout_shipping.php', headers=headers)
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'es-ES,es;q=0.5',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.anfittingsdirect.com/create_account.php',
    'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Brave";v="146"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
    # 'cookie': 'cookie_test=please_accept_for_session; osCsid=4051906790886dd6f332098f68f881eb',
}

response = session.get('https://www.anfittingsdirect.com/checkout_payment.php', headers=headers)
headers = {
    'accept': '*/*',
    'accept-language': 'es-ES,es;q=0.5',
    'authorization': f'Bearer {bearer}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'priority': 'u=1, i',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Brave";v="146"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
}

json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'dropin2',
        'sessionId': str(uuid.uuid4()),
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': '5566920440024911',
                'expirationMonth': '12',
                'expirationYear': '2028',
                'cvv': '346',
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

response = session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data).json()
toke1 = response['data']['tokenizeCreditCard']['token']
print(toke1)
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'es-ES,es;q=0.5',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.anfittingsdirect.com',
    'priority': 'u=0, i',
    'referer': 'https://www.anfittingsdirect.com/checkout_payment.php',
    'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Brave";v="146"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
    # 'cookie': 'cookie_test=please_accept_for_session; osCsid=4051906790886dd6f332098f68f881eb',
}

data = {
    'action': 'process',
    'shipping': 'table_table',
    'coupon': '',
    'payment': 'braintree_jh_creditcard',
    'btjh_credit_card_nonce': toke1,
    'comments': '',
    'accept_terms': '1',
    'user_clicked_complete_order': 'COMPLETE ORDER',
}

response = session.post('https://www.anfittingsdirect.com/checkout_payment.php', headers=headers, data=data)
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'es-ES,es;q=0.5',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.anfittingsdirect.com/checkout_payment.php',
    'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Brave";v="146"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
    # 'cookie': 'cookie_test=please_accept_for_session; osCsid=4051906790886dd6f332098f68f881eb',
}

response = session.get('https://www.anfittingsdirect.com/checkout_process.php', headers=headers)

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'es-ES,es;q=0.5',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.anfittingsdirect.com/checkout_payment.php',
    'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Brave";v="146"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
    # 'cookie': 'cookie_test=please_accept_for_session; osCsid=4051906790886dd6f332098f68f881eb',
}

response = session.get('https://www.anfittingsdirect.com/checkout_payment.php', headers=headers).text
print(response)