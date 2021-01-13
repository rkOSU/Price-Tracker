import time

import requests
from bs4 import BeautifulSoup
import smtplib

# Website URL
# Ask user for input
print('Enter the URL for the item: ')
URL = input()

#URL = 'https://www.amazon.com/ROMOSS-Portable-Charger-Outputs-Compatible/dp/B07H5T9J4L/ref=sr_1_1_sspa?dchild=1&keywords=battery+pack&qid=1610427778&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExOUE4REdKVTdZTEJZJmVuY3J5cHRlZElkPUEwNDgyNjQ5MU9GOEIyUUo4M1cxTiZlbmNyeXB0ZWRBZElkPUEwOTE3NTkwODBZQzBDQUhNNTBOJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36', 'Cache-Control': 'no-cache', "Pragma": "no-cache"}



def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    try:
        # Scrape links of items
        links = []
        for item in soup.findAll("a", {"class":"a-size-base a-link-normal a-text-normal"}):
            
            links.append(item["href"])
        
        # Scrape prices of items
        prices = []
        for item in soup.findAll("span", {"class":"a-offscreen"}):
            
            prices.append(item.get_text().strip())
        #print(prices)

        # Scrape names of items
        names = []
        for item in soup.findAll("span", {"class":"a-size-base-plus a-color-base a-text-normal"}):
            
            names.append(item.get_text().strip())
        # Build item array
        item_array = []
        for i in range(0, len(names)):
            item_info = []
            item_info.append(prices[i])
            item_info.append(names[i])
            item_info.append(links[i])
            item_array.append(item_info)
            print(item_info)

        print(item_array)
        # Sort list of items
        item_array.sort()

        print(item_array[:3])
        '''
        #Scrape name of item
        title = soup.find(id="productTitle").get_text().strip()
        # Extract price of item
        print(title)

        price =  soup.find(id="priceblock_ourprice").get_text()
        num_price = float(price[1:])
        print (num_price)


        #if(num_price < 170):
        #    send_email(title, price)

        #print(num_price)
        #print(title.strip())
        '''
        return 1
    except:
        print("Error scraping!")
        return -1
    

def send_email(product_name, price):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('rajkondaveeti3@gmail.com', 'eynbnrlxbyztigtx')

    subject = "Price has fallen!"
    body = 'Item: {}\nCurrent Price: {}\n\nLink: {}'.format(product_name, price, URL)

    msg = f"Subject: {subject}\n\n{body}"
    #server.sendmail('rajkondaveeti3@gmail.com',
    #                'rajkondaveeti3@gmail.com',
    #                msg)
    print("Email sent!")

    server.quit()

flag = True
while flag:
    if check_price() == 1: flag = False
