import pandas as pd

def extract_table(table,conn):
 
    df = pd.read_sql(f"SELECT a.*, now() as fecha_carga FROM {table} a", con = conn)
 
    return df