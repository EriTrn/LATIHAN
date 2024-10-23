import os
import urllib.request as urllib2
import json

while True:
    ip = input("alamat ip mu: ")
    url = "https://ip-api.com/json/"
    response = urllib2.urlopen(url+ip)
    data = response.read()
    values = json.loads(data)

    print("IP: " + values["query"])
    print("city: " + values["city"])
    print("ISP: " + values["isp"])
    print("Country: " + values ["country"])
    print("Region: " + values["region"])
    print("Timezone: " + values["timezone"])
    break