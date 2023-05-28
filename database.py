import sqlite3
from stock import Stock

class Database:
    def __init__(self) :
        self.__con = sqlite3.connect("db/sqlite3/bhavDB")

    def createTables(self) :
        table = """ CREATE TABLE IF NOT EXISTS security (
            symbol TEXT NOT NULL,
            exchange TEXT NOT NULL,
            series CHAR(10),
            trade_date TEXT NOT NULL,
            open REAL NOT NULL,
            high REAL NOT NULL,
            low REAL NOT NULL,
            close REAL NOT NULL,
            prev_close REAL NOT NULL,
            volume REAL NOT NULL,
            dividends REAL NOT NULL,
            stock_splits REAL NOT NULL
        ); """

        index1 = """ CREATE UNIQUE INDEX IF NOT EXISTS idx_symbol on security (symbol, exchange, 
        series, trade_date );"""
        cursor = self.__con.cursor()
        self.__con.cursor().execute(table)
        self.__con.commit()
        cursor.close()
        cursor_index = self.__con.cursor()
        cursor_index.execute(index1)
        self.__con.commit()
        cursor_index.close()
    
    def insertEntry(self,index,stock) :
        try: 
            sqlite_insert_with_param = """INSERT INTO security
                          (symbol, exchange, series, trade_date, open, high, 
                          low, close, prev_close,volume, dividends,
                          stock_splits ) 
                          VALUES (?, ?, ?, ?, ?,?,?,?,?,?,?,?);"""
            data_tuple = ( stock.symbol,  'NSE', 'EQ' , index, stock.Open,
                      stock.High, stock.Low, stock.Close,
                      0.0, stock.Volume, stock.Dividends, 0.0 )
            cursor = self.__con.cursor()
            cursor.execute(sqlite_insert_with_param, data_tuple)
            self.__con.commit()
            cursor.close()
        except sqlite3.IntegrityError as err:
            print(f"Ignoring error: {err}")