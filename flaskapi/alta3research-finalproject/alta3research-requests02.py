#!/usr/bin/env python3
import requests
from pprint import pprint

URL= "http://127.0.0.1:2224/data"

resp= requests.get(URL).json()
def skills():
    for x in resp['programming skills']:
        print (x)

for x in resp:
    print(f"{x['student']}'s age is {x['age']}. He likes {x['alias']} and his favorite programming language is {x['programming skills']}.")

pprint(resp)