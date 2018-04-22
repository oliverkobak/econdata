from c_get_data import GetData

import xlrd
import mysql.connector

data = GetData()
#data.downloadData("https://www.imf.org/external/pubs/ft/weo/2017/01/weodata/WEOApr2017all.xls","test_data.xls")
data.importFileToDb("t# # est_data.xls")
