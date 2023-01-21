_DB_FILE = "sales.sqlite"

def download_db(db_file=_DB_FILE):
    import os
    if os.path.exists(_DB_FILE):
        return
    import gdown
    id = "1Nj4iinR4jC9D0u43CYi7_aP-HaequDi8"
    url = f"https://drive.google.com/uc?id={id}"
    gdown.download(url, db_file, quiet=False)

download_db(_DB_FILE)

def query(sql):
    import pandas as pd
    import sqlite3
    con = sqlite3.connect(_DB_FILE)
    return pd.read_sql_query(sql, con)  
