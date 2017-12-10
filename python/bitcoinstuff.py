import json
from urllib.request import Request, urlopen

url = "https://www.worldcoinindex.com/apiservice/json?key=5cukMpmjhFXhd4ZN779xKfqIbaNpqk"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urlopen(req)
data = json.loads(response.read())


my_coins = ['Zencash', 'Bitcoin', 'Litecoin', 'Vertcoin', 'Digitalprice', 'Ethereum', 'Diamond', 'Monero', 'Bitcoingold',
            'Omisego', 'Factom', 'Neo', 'Iota', 'Request', 'Ark', 'Bat', 'Nem']

my_amount = {'Bitcoin': .0923, 'Zencash': 3.6, 'Litecoin': 1.08, 'Vertcoin': 51, 'Digitalprice': 5751, 'Ethereum': .578,
             'Diamond': 6, 'Monero': .4, 'Bitcoingold': .05, 'Omisego': 15, 'Factom': 1, 'Neo': 1.47, 'Iota': 25, 'Request': 0,
             'Ark': 10, 'Bat': 250, 'Nem': 84}

portfolio_total = 0


for market in data['Markets']:
    for coin in my_coins:
        if market['Name'] == coin:
            amount = (market["Price_usd"])* my_amount[market['Name']]
            portfolio_total += amount
            print(market["Name"] + ' : $' + format(market["Price_usd"], '.2f') + ' per coin. That\'s worth $' + format(amount, '.2f') + ' to me.')
print('\n')
print(f'My portfolio is worth ${portfolio_total}.')