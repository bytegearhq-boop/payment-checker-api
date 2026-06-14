import uuid
import names
import json
from dataclasses import dataclass
import random
from requests import Session
from bs4 import BeautifulSoup

class ConfigsPAge:
    def QueryText(self, data:str = None, chainOne:str = None, chainTwo:str = None):
        
            self.uophs = data[ data.index(chainOne) + len (chainOne):data.index(chainTwo,  data.index(chainOne) + len (chainOne))]
            try:
                return self.uophs
            
            except: 
                return 'value not found' 
    @classmethod
    def SessionId(self):
        self.id = str(uuid.uuid4())
        return self.id
    @classmethod
    def RandomName(self,dato:str=None):
        if dato == 'username': 
            self.username = "{}{}{}".format(
                    names.get_first_name(),
                    names.get_last_name(),
                    random.randint(1000000,9999999)
                    )
            return self.username
         
        elif dato == 'email': 
            self.email = "{}{}{}@gmail.com".format(
                names.get_first_name(),
                names.get_last_name(),
                random.randint(1000000,9999999)
            )
            return self.email
        
        elif dato == 'password': 
            self.password = "{}{}#{}".format(
                names.get_first_name(),
                names.get_last_name(),
                random.randint(1000000,9999999)
            )
            return self.password
        
        elif dato == 'numero':
            self.number = ''.join([str(random.randint(0, 9)) for _ in range(10)])
            return self.number
        
        else:
            return 'valores incorrectos: >>>   BehaviorsBraintree().RandomName("username")'
    
    
    
    def SaveResponseHhml(self, response:str):
        with open("ResponseHhml.html", "w", encoding="utf-8") as f:
            f.write(response)

@dataclass
class autnet_woo:
    def main(self,card):
            
        self.email = ConfigsPAge().RandomName('email')
        self.password = ConfigsPAge().RandomName('password')
        self.name = ConfigsPAge().RandomName('username')

        self.ccs = card.split('|')

        if self.ccs[0].startswith("4"): self.brand = "VISA"
        if self.ccs[0].startswith("3"): self.brand = "AMEX"
        if self.ccs[0].startswith("6"): self.brand = "DISCOVER"
        elif self.ccs[0].startswith("5"): self.brand = "MASTER_CARD"
            
        session = Session()
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'es-ES,es;q=0.5',
            'cache-control': 'max-age=0',
            'priority': 'u=0, i',
            'referer': 'https://www.gourmetduvillage.com/shop/',
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
            # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-03-28%2002%3A22%3A27%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.gourmetduvillage.com%2Fproduct%2Fsnowglobe-set-of-6%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-03-28%2002%3A22%3A27%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.gourmetduvillage.com%2Fproduct%2Fsnowglobe-set-of-6%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F146.0.0.0%20Safari%2F537.36; wp-wpml_current_language=en; wp_woocommerce_session_30b1fcdbaf6eb35ca4f527e7be5c2ae3=t_fdfdfb4b76c41f0ab6b9d5347ff107%7C1774837367%7C1774750967%7C%24generic%24CjSARIFJ-hyaAHzcWtjc4vIiVpduuwht7rjuihHz; sbjs_session=pgs%3D14%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.gourmetduvillage.com%2Fproduct%2Fmexican-street-corn-dip%2F',
        }

        response = session.get('https://www.gourmetduvillage.com/product/mexican-street-corn-dip/',  headers=headers)
        
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'es-ES,es;q=0.5',
            'cache-control': 'max-age=0',
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryNOMrWgozVcBmPbKs',
            'origin': 'https://www.gourmetduvillage.com',
            'priority': 'u=0, i',
            'referer': 'https://www.gourmetduvillage.com/product/mexican-street-corn-dip/',
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
            # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-03-28%2002%3A22%3A27%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.gourmetduvillage.com%2Fproduct%2Fsnowglobe-set-of-6%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-03-28%2002%3A22%3A27%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.gourmetduvillage.com%2Fproduct%2Fsnowglobe-set-of-6%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F146.0.0.0%20Safari%2F537.36; wp-wpml_current_language=en; wp_woocommerce_session_30b1fcdbaf6eb35ca4f527e7be5c2ae3=t_fdfdfb4b76c41f0ab6b9d5347ff107%7C1774837367%7C1774750967%7C%24generic%24CjSARIFJ-hyaAHzcWtjc4vIiVpduuwht7rjuihHz; sbjs_session=pgs%3D15%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.gourmetduvillage.com%2Fproduct%2Fmexican-street-corn-dip%2F',
        }

        files = {
            'quantity': (None, '1'),
            'add-to-cart': (None, '110355'),
            'gtm4wp_product_data': (None, '{"internal_id":110355,"item_id":110355,"item_name":"Mexican Street Corn Dip","sku":"GDIPXSC","price":4.4900000000000002131628207280300557613372802734375,"stocklevel":null,"stockstatus":"instock","google_business_vertical":"retail","item_category":"Dips","id":110355}'),
        }

        response = session.post(
            'https://www.gourmetduvillage.com/product/mexican-street-corn-dip/',
            headers=headers,
            files=files,
        )

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'es-ES,es;q=0.5',
            'priority': 'u=0, i',
            'referer': 'https://www.gourmetduvillage.com/product/mexican-street-corn-dip/',
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
            # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-03-28%2002%3A22%3A27%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.gourmetduvillage.com%2Fproduct%2Fsnowglobe-set-of-6%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-03-28%2002%3A22%3A27%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.gourmetduvillage.com%2Fproduct%2Fsnowglobe-set-of-6%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F146.0.0.0%20Safari%2F537.36; wp-wpml_current_language=en; wp_woocommerce_session_30b1fcdbaf6eb35ca4f527e7be5c2ae3=t_fdfdfb4b76c41f0ab6b9d5347ff107%7C1774837367%7C1774750967%7C%24generic%24CjSARIFJ-hyaAHzcWtjc4vIiVpduuwht7rjuihHz; woocommerce_items_in_cart=1; woocommerce_cart_hash=4541e302ae1e55bb887a7e6b31749684; sbjs_session=pgs%3D16%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.gourmetduvillage.com%2Fproduct%2Fmexican-street-corn-dip%2F',
        }

        response = session.get('https://www.gourmetduvillage.com/cart/', headers=headers).text
        cart = ConfigsPAge().QueryText(response, 'name="woocommerce-cart-nonce" value="', '"')
        print(cart)
cc = input('cc: ')
chk = autnet_woo().main(cc)
print(chk)