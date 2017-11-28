import json
from urllib.request import Request, urlopen

url = "https://www.worldcoinindex.com/apiservice/json?key=5cukMpmjhFXhd4ZN779xKfqIbaNpqk"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urlopen(req)
data = json.loads(response.read())


my_coins = ['Zencash', 'Bitcoin', 'Litecoin', 'Vertcoin', 'Digitalprice', 'Ethereum', 'Diamond', 'Monero', 'Bitcoingold']

for market in data['Markets']:
    for coin in my_coins:
        if market['Name'] == coin:
            print(market["Name"] + ' : ' + str(market["Price_usd"]) + ' dollars.')

