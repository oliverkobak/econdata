#!/usr/bin/python

from c_analyse_input import AnalyseInput

query = input("Enter country: ")
elements = query.split()
key = AnalyseInput()
key.analyse_query(elements)
# key.compute()
print(key.analysed_query)
