import requests
import os 
import json
import sys
from dotenv import load_dotenv
load_dotenv()

def d(o):
    print(o)

def dd(o):
    d(o)
    quit()

key = os.getenv("KEY")
url = "https://api.companieshouse.gov.uk"
term = sys.argv[1]

for i in range(1):
    resp = requests.get(url + "/search", params={"q":term, "items_per_page":100, "start_index":i*100}, auth=(key, ""))

    j = json.loads(resp.text)
    for item in j['items']:
        locality = item['address'].get('locality', "")
        post_code = item['address'].get('postal_code', "")
        if (str(locality).startswith('London')) and (str(post_code).startswith('EC')):
            print(item['title'], locality, post_code)

