import pandas as pd
from stock import Stock 
from database import Database as db 
from datetime import datetime

dbConn = db()
df = dbConn.getStockDataAsDf("2023-05-25")
records = df.to_dict(orient='records')
for row in records:
    print(row)
    print(row['symbol'])