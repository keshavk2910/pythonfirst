import urllib.request as urllib2
from bs4 import BeautifulSoup
import csv
import gspread
import json
from oauth2client.client import SignedJwtAssertionCredentials
from datetime import datetime
from forex_python.converter import CurrencyRates

conv = CurrencyRates()
usdinr = conv.get_rate('USD', 'INR')
print (usdinr)

dt = datetime.now()
hours = dt.hour
minute = dt.minute
day = dt.day
month = dt.month

with open('index.csv', 'a') as csv_file:
 writer = csv.writer(csv_file)
 writer.writerow([usdinr , hours,minute])
 
json_key = json.load(open('cred.json')) # json credentials you downloaded earlier
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope) # get email and key from creds
file = gspread.authorize(credentials) # authenticate with Google
sheet = file.open("indexpy").sheet1 # open sheet
row = [usdinr,day,month,hours,minute]
index = 2
sheet.insert_row(row, index)

