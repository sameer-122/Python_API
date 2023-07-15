from requests import Session
import secrets
import json
import datetime


# url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
# headers = {
#   'Accepts': 'application/json',
#   'X-CMC_PRO_API_KEY': secrets.API_KEY,
# }
# r = requests.get(url, headers=headers)
# pp( r.json()['data']
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    with open('coin.txt', 'w') as f:
        time = datetime.datetime.now().time().strftime('%H:%M:%S')
        print(time)
        input = 'fetched time: '+ time + '\n' + text
        f.write(input)
    print(text)

class CMC:
    def __init__(self, token):
        self.apiurl = 'https://pro-api.coinmarketcap.com'
        self.headers = { 'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': token }
        self.session = Session()
        self.session.headers.update(self.headers)

    def getAllCoins(self):
        url = self.apiurl + '/v1/cryptocurrency/map'
        r = self.session.get(url)
        data = r.json()['data']
        return data
    def getPrice(self, symbol):
        url = self.apiurl + '/v2/cryptocurrency/quotes/latest'
        parameters = { 'symbol': symbol }
        r = self.session.get(url, params=parameters)
        data = r.json()['data']
        price = data['BTC'][0]['quote']['USD']['price']
        return data
if __name__ == '__main__':
    cmc = CMC(secrets.API_KEY)

    str = '*'*100
    print(str)
    jprint(cmc.getAllCoins())
    print(str)
    # pp(cmc.getAllCoins())
    # pp(cmc.getPrice('BTC'))