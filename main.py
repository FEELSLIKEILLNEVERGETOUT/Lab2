import requests
import json
import time
d={}

def getinfo():
    b=requests.get('https://blockchain.info/ru/ticker').text
    d=json.loads(b)
    while True:
        val=input()
        for key in d:
            if key ==val:
                print(key, d[key])
        time.sleep(5)
getinfo()