import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

api_key = False
if api_key is False:
  serviceirl = "http://py4e-data.dr-chuck.net/geojson?"
else:
  serviceurl = "https://maps.googleapis.com/maps/api/place/textsearch/json"

  while True:
    address = input('Enter location:')
    if len(address)<1: break

    url = serviceurl + urllib.parse.urlencode(
      
      {'address':address})
    print('retriving',url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('retrived', len(data), 'characters')