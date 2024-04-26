import pandas as pd
from stock import Stock
from database import Database as db
from datetime import datetime

dbConn = db()
# df = dbConn.getStockDataAsDf("2023-05-25")
# records = df.to_dict(orient='records')
# for row in records:
#     print(row)
#     print(row['symbol'])


df = dbConn.get_weekly_closing(5)
df['week_of_year'] = df['week_of_year'].astype(int)
df['prev_week_of_year'] = df['week_of_year'] - 1
df = pd.merge(df, df[['symbol', 'week_of_year', 'close']], how='left', left_on=['symbol', 'prev_week_of_year'], right_on=['symbol', 'week_of_year'], suffixes=('', '_prev'))
df['close_prev'] = df['close_prev'].fillna(df['close'] -1)
df['is_greater_than_prev_week'] = df.apply(lambda row: 'Y' if row['close'] > row['close_prev'] else 'N', axis=1)
result_df = df.groupby('symbol')['is_greater_than_prev_week'].apply(lambda x: 'Y' if all(x == 'Y') else 'N').reset_index(name='result')
symbols_Y = result_df[result_df['result'] == 'Y']['symbol'].tolist()
symbols_N = result_df[result_df['result'] == 'N']['symbol'].tolist()

print("Symbols with increasing week on week close:", symbols_Y)
