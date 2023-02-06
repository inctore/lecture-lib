_DB_FILE = "sales.sqlite"


def download_db(db_file=_DB_FILE):
    import os
    if os.path.exists(_DB_FILE):
        return
    import gdown
    id = "1Nj4iinR4jC9D0u43CYi7_aP-HaequDi8"
    url = f"https://drive.google.com/uc?id={id}"
    gdown.download(url, db_file, quiet=False)


def query(sql):
    import pandas as pd
    import sqlite3
    con = sqlite3.connect(_DB_FILE)
    return pd.read_sql_query(sql, con)


def download_csv():
    import sqlite3
    import pandas as pd
    con = sqlite3.connect(_DB_FILE)
    sales = pd.read_sql_query("""
    select * from sales
    """, con)
    sales.to_csv("sales.csv", index=False)

    stores = pd.read_sql_query("""
    select * from stores
    """, con)
    stores.to_csv("stores.csv", index=False)

    features = pd.read_sql_query("""
    select * from features
    """, con)
    features.to_csv("features.csv", index=False)
