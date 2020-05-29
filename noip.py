#!/usr/bin/env python
# inspired by https://gist.github.com/bhaskarkc/c2f8c2cabd2a3991772f108f68dffcde
import requests, os

username = os.getenv('NOIP_USER')
password = os.getenv('NOIP_PASS')
hostname = os.getenv('NOIP_DOMAIN') #"adrian9.hopto.org" # your domain name hosted in no-ip.com
print(hostname)

myip = "40.89.169.60"

# https://www.noip.com/integrate/request.
def update_dns(config):
    print("Calling noip")
    r = requests.get("http://{}:{}@dynupdate.no-ip.com/nic/update?hostname={}&myip={}".format(*config))

    if r.status_code != requests.codes.ok:
        print(r.content)
    else:
        print("noip call OK")

# update_dns( (username, password, hostname, myip) )
