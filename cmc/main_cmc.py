# RTM (READ THE DOCUMENTATION https://coinmarketcap.com/api/documentation/v1/#)
# Import modules and API key
# Test a basic request
# Build up a class, so we can easily make the REST API calls
import datetime
import sys
import requests
import secrets
from pprint import pprint as pp
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)        # convert to a formatted string from Python JSON object
    with open('coin.txt', 'w') as f:
        time = datetime.datetime.now().time().strftime('%H:%M:%S')
        input = f'fetched time: {time}' + '\n' + text
        f.write(input)
    # print(text)

def insertion_sort(list) :   # O(N*N)
    l = list
    for i in range(1,len(list),1):
        j=i
        while l[j]['rank'] < l[j-1]['rank'] and j>0:
            l[j], l[j-1] = l[j-1], l[j]
            j-=1
    return l

def counting_sort(l:list) :     # linear order: O(N + k) where k= (max-min)
    mx = -1
    mn = sys.maxsize
    for x in l: mx = max(mx,x['rank'])
    for x in l: mn = min(mn,x['rank'])
    print('min:', mn,', max:',mx)
    print('Total Coins:', len(l))

    count = [[0,0] for x in range(mx-mn+1)]
    for x in l:
        count[x['rank']-mn][0]+= 1
        count[x['rank']-mn][1] = x
    l = []
    for i in range(len(count)):
        while count[i][0]:          # assuming 2 coins ranks could be same, but practically it's unique.
            l.append(count[i][1])
            count[i][0]-=1
    return l

def sort_cmc():
    with open('coin.txt', 'r') as f:
        time = f.readline()
        text = f.read()
    list = json.loads(text)     # converting string to its python object, here list
    print('type after json.loads() in sort_cmc: ',type(list))
    l = counting_sort(list)        # sorting on basis of coin rank

    stext = json.dumps(l, indent=4, sort_keys=False)   # Again converting back to string format to write in newfile
    datetime_obj = datetime.datetime.now()
    time = datetime.datetime.now().time().strftime('%H:%M:%S')
    stext = f'sorted time: {time}, Total Coins: {len(l)}' + '\n'+ stext
    with open('coinRankSorted.txt', 'w') as f:
        f.write(stext)

if __name__ == '__main__':
    base_url = 'https://pro-api.coinmarketcap.com'
    url = base_url +'/v1/cryptocurrency/map'
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': secrets.API_KEY,
    }
    parameters = {       # see the correct parameter for this url
        'start': '1',
        'limit': '5000',
        'convert': 'USD'
    }
    response = requests.get(url, headers=headers)
    r = response

    print(r.status_code, end='\n\n')
    jprint(r.json()['data'])   # r.json() parses the body of response 'r' into json object

    sort_cmc()
    print('Over')

    # for i in range(5):
    #   pp( r.json()['data'][i] )
    #   print('\n')