import os

from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

raw_data_string = os.getenv("RAW_DATA")
staging_data_string = os.getenv("STAGING_DATA")
dwh_data_string = os.getenv("DWH_DATA")

def get_source_engine():
    engine = create_engine(raw_data_string)
    return engine

def get_staging_engine():
    engine = create_engine(staging_data_string)
    return engine

def get_dwh_engine():
    engine = create_engine(dwh_data_string)
    return engine

print(get_source_engine().connect())