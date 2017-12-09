import json
from urllib.request import Request, urlopen

url = "https://www.worldcoinindex.com/apiservice/json?key=5cukMpmjhFXhd4ZN779xKfqIbaNpqk"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urlopen(req)
data = json.loads(response.read())


my_coins = ['Zencash', 'Bitcoin', 'Litecoin', 'Vertcoin', 'Digitalprice', 'Ethereum', 'Diamond', 'Monero', 'Bitcoingold', 'Omisego', 'Factom', 'Neo', 'Iota', 'Request']
my_amount = {'Bitcoin': .09, 'Zencash': 3.5, 'Litecoin': 1, 'Vertcoin': 51, 'Digitalprice': 5751, 'Ethereum': .5, 'Diamond': 6, 'Monero': .4, 'Bitcoingold': .05, 'Omisego': 15, 'Factom': 1, 'Neo': 1.3, 'Iota': 25, 'Request': 0}
portfolio_total = 0


for market in data['Markets']:
    for coin in my_coins:
        if market['Name'] == coin:
            amount = (market["Price_usd"])* my_amount[market['Name']]
            portfolio_total += amount
            print(market["Name"] + ' : ' + str(market["Price_usd"]) + ' dollars per coin. That\'s worth ' + str(amount) + ' to me.')

print(f'My portfolio is worth {portfolio_total}.')