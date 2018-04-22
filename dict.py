#!/usr/bin/python

import json

with open("countries.json", 'r') as json_file:
    countries = json.load(json_file)

query = input("Enter query: ")

def search(values, searchFor):
    for k in values:
        for v in values[k]:
            if searchFor == v:
                return  k
    return None

print(search(countries, query))
