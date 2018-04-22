import requests
import pandas
from bs4 import BeautifulSoup
import json
import csv

l = {}
r = requests.get("http://www.worldatlas.com/aatlas/ctycodes.htm")
c = r.content

soup = BeautifulSoup(c, "html.parser")
soup.find("tr").extract()
all = soup.find_all("tr")

for item in all:
    d = {}
    d[item.find_all("td")[2].text] = [item.find_all("td")[0].text, item.find_all("td")[1].text, item.find_all("td")[2].text]
    l.update(d)
    df = pandas.DataFrame(l)

    with open('countries.json', 'w') as fp:
        json.dump(l, fp, sort_keys=True, indent=4)
