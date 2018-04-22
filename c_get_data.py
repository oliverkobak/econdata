#!/usr/bin/python

import urllib.request
import pandas as pd
#import MySQLdb

class GetData(object):
    def downloadData(self, url, file_name):
        urllib.request.urlretrieve(url, file_name)

    def importFileToDb(self, file_name):
        data = pd.read_excel(file_name)
        print(data)
        #book = xlrd.open_workbook(file_name)
        #sheet = book.sheet_by_name("WEOApr2017all")

        #database = MySQLbd.connect(host = "localhost", user = "oliver", passwd = "oliverkobak", db = "econdata_raw")
        #cusrsor = database.cursor()

        query = """INSERT INTO weo_all 
                    (
                        weo_country_code,
                        iso,
                        weo_subject_code,
                        country,
                        subject_description,
                        subject_notes,
                        units,
                        scale,
                        country_series_specific_note,
                        1980,
                        1981,
                        1982,
                        1983,
                        1984,
                        1985,
                        1986,
                        1987,
                        1987,
                        1988,
                        1989,
                        1990,
                        1991,
                        1992,
                        1993,
                        1994,
                        1995,
                        1996,
                        1997,
                        1998,
                        1999,
                        2000,
                        2001,
                        2002,
                        2003,
                        2004,
                        2005,
                        2006,
                        2007,
                        2008,
                        2009,
                        2010,
                        2011,
                        2012,
                        2013,
                        2014,
                        2015,
                        2016,
                        2017,
                        2018,
                        2019,
                        2020,
                        2021,
                        2022,
                        estimates_starts_after
                    )
                    VALUES
                    (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

#test = GetData()
#test.downloadData("data/imf_full_data.xls")
#test.importFile("data/imf_full_data.xls")
