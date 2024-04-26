import yfinance as yf
import pandas as pd
from stock import Stock 
from database import Database as db 
from datetime import datetime


dbConn = db()
dbConn.createTables()

#tcs = yf.Ticker("TCS.NS")
#data= tcs.history(period="2y")
#print(data)

def load_db():
  scrips = pd.read_csv("nse_scrips.txt")
  f = open("nse_scrips.txt", "r")
  for scrip in f:
    orignal_scrip = scrip.strip()
    scrip = scrip.strip() + ".NS"
    y_scrip = yf.Ticker(scrip)
    print(f"Going to query: {scrip}")
    scrip_data = y_scrip.history(period="2y")

    index_records = scrip_data.to_dict(orient='index')
    for index in index_records:
      stock = Stock(orignal_scrip,**index_records[index])
      date = index.to_pydatetime()
      dbConn.insertEntry(date,stock)
    print(f"Inserted data into table for: {orignal_scrip}")

if __name__ == '__main__':
  load_db()
