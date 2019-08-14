#!/usr/bin/env python3

import base64   
import json        
import sseclient
import requests
from twitter import OAuth, Twitter
import credentials

oauth = OAuth(
        credentials.ACCESS_TOKEN,
        credentials.ACCESS_SECRET,
        credentials.CONSUMER_KEY,
        credentials.CONSUMER_SECRET
    )
t = Twitter(auth=oauth)
                
BITSOCKET_URL = 'https://bitsocket.bch.sx/s/'

def query_bitsocket(query, fn):
    json_string = bytes(json.dumps(query), 'utf-8')
    url = base64.b64encode(json_string)
    r = requests.get(BITSOCKET_URL + url.decode('utf-8'), stream=True)

    client = sseclient.SSEClient(r)
    for evt in client.events():
        fn(json.loads(evt.data))
                
def bitsocket_handler(j):
  if j['data'] == []:
    pass
  else:
    try:
      print(j['data'])
      t.statuses.update(status=(j['data']))
    except:
      pass        
                
                
query_bitsocket({
  "v": 3,
  "q": {
    "db": ["u"],
    "find": {
      "in.e.a": "qxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "out.h1": "6d02"
    }
  },
  "r": {
    "f": ".[] | .out[] | select(.b0.op? == 106) | .s2"
  }             
}, bitsocket_handler)

