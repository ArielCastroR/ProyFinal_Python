import pandas as pd
import sqlalchemy as db
from sqlalchemy import text
 
def connect_cyber_db():
    
    engine = db.create_engine("mysql://root:root1988@127.0.0.1/cyber")
    conn = engine.connect()
 
    return conn

def connect_dw_cyber():
    engine = db.create_engine("mysql://root:root1988@127.0.0.1/dwh_lancenter")
    conn = engine.connect()
 
    return conn