import time

import requests
from bs4 import BeautifulSoup
import smtplib
from login import getLogin

# Website URL
# TODO: ask user for link

URL = 'https://www.amazon.com/Pet-Qwerks-BarkBone-Peanut-Butter/dp/B07PX3T3BF/ref=sr_1_19_sspa?dchild=1&keywords=dog+toy&qid=1600658055&sr=8-19-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyVkdGWjFCRjAxUVA4JmVuY3J5cHRlZElkPUEwODUyNDU2MUM2RzdBS0VUWTVURyZlbmNyeXB0ZWRBZElkPUEwMDM1OTYzMlZGMDM5VE9KT0lEViZ3aWRnZXROYW1lPXNwX210ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/85.0.4183.102 Safari/537.36'}

title = ""

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')


    # Extract tile of item
    title_i = soup.find(id="productTitle")
    print(title_i)

    title = soup.find(id="productTitle").get_text()
    # Extract price of item

    price =  soup.find(id="priceblock_ourprice").get_text()
    num_price = float(price[1:])


    if(num_price < 170):
        send_email(title, price)

    print(num_price)
    print(title.strip())

def send_email(product_name, price):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    login_info = getLogin()
    server.login(login_info[0], login_info[1])

    subject = "Price has fallen!"
    body = 'Item: {}\nCurrent Price: {}\n\nLink: {}'.format(product_name, price, URL)

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('rajkondaveeti3@gmail.com',
                    'boone.200@osu.edu',
                    msg)
    print("Email sent!")

    server.quit()

while True:
    check_price()
