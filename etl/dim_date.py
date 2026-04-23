from sqlalchemy import text

from config import get_dwh_engine
import pandas as pd

start_date = '2013-01-01'
end_date = '2016-05-31'

df = pd.DataFrame({'full_date': pd.date_range(start_date, end_date)})
df['date_key'] = df['full_date'].dt.strftime('%Y%m%d').astype(int)
df = df[['date_key', 'full_date']]
df['year'] = df['full_date'].dt.year
df['month'] = df['full_date'].dt.month
df['month_name'] = df['full_date'].dt.month_name()
df['day'] = df['full_date'].dt.day
df['day_name'] = df['full_date'].dt.day_name()
df['weekday'] = df['full_date'].dt.weekday
df['is_weekend'] = df['weekday'] >=5
df['quarter'] = df['full_date'].dt.quarter

print(df)

engine = get_dwh_engine()

df.to_sql('dim_date', con=engine, if_exists='replace', index=False)

with engine.connect() as conn:
    res = conn.execute(text("create index if not exists dim_date_date_key_index on dim_date(date_key);"))
    print("Index on date key - created.")
    conn.commit()