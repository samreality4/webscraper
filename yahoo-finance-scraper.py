import requests
from bs4 import BeautifulSoup

res = requests.get('https://finance.yahoo.com/quote/NIO?p=NIO&.tsrc=fin-srch')
soup = BeautifulSoup(res.text, "html.parser")

current_price = soup.select("span[data-reactid='50']")[0].text
ask = soup.select("span[data-reactid='113']")[0].text
bid = soup.select("span[data-reactid='108']")[0].text

ask_array = ask.split("x")
bid_array = ask.split("x")

ask_price, ask_volume = float(ask_array[0].strip()), int(ask_array[1].strip())
bid_price, bid_volume = float(bid_array[0].strip()), int(bid_array[1].strip())
print(ask_price)
