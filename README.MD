## Getting Started
This program uses Python yfinance library to pull Indian stock market data and write it into 
sqlite database.

### Setup DB

Create a directory for sqlite DB

  ```sh
  mkdir db/sqlite3/bhavDB
  ```

All the NSE stock data will be stored into this DB.

### Setup Python environment
Run below commands:

  ```sh
  python3 -m venv .venv
  source ./.venv/bin/activate
  python3 -m pip install yfinance
  ```

### What are all scripts and what they do.

#### load_mkt_data.py

1. nse_scrips.txt contains list of all NSE listed securties in EQ series
2. For each scrip it calls yfinance API and gets market data 
3. This market data is then loaded into sqlite db

#### TODO
1. Support for NSE SME
2. Support for BSE data
3. Support to directly pull data from NSE, BSE websites and reitire yfinance
4. Variouse fiters on this data using Pandas library
