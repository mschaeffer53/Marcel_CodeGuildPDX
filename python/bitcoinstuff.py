import json
from urllib.request import Request, urlopen

url = "https://www.worldcoinindex.com/apiservice/json?key=5cukMpmjhFXhd4ZN779xKfqIbaNpqk"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urlopen(req)
data = json.loads(response.read())


for market in data['Markets']:

    print(market["Name"] + ' : ' + str(market["Price_usd"]))

