#!/usr/bin/env python

import csv
import json
import requests

url ='https://interview-0159fb3195.interview.vme.dev/api/v1/client'

with open('~/clients.csv','r') as clientsfile:
     reader = csv.DictReader(clientsfile)

for records in reader:
    output.append(records)

with open('~/clientsJ.json','w')as outfile:
     json.dump(output,outfile,sort_keys=True, indent=4)

with open('~/clientsJ.json','r')as infile:
     indata = json.load(infile)

for data in indata:
    reqclientspos= requests.post(url, json=data)
    print(reqclientspos, reqclientspos.text)

clientlist= requests.get(url)
print(clientlist, clientlist.text)
