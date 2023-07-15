# RTM: https://www.weatherapi.com/docs/
import requests
from cmc import secrets
from pprint import pprint as pp
base_url = 'http://api.weatherapi.com/v1'
# url = base_url + '/current.json'
url = 'http://api.weatherapi.com/v1/current.json?key=91a7bb4cbe804e2ab83171912231207&q=bulk'
# q = secrets.API_KEY
location = 'pune'
headers = { 'Content-Type': 'application/json',
            'q': secrets.API_KEY,
            'location' : 'pune',
            'ded': 'dedd'}
r = requests.get(url,headers=headers)
pp(r.status_code)
pp(r.json())