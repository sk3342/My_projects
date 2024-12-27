import pandas as pd
from sqlalchemy import create_engine

def query_data(db_url):
    """Query action counts from MySQL database."""
    engine = create_engine(db_url)
    query = "SELECT * FROM action_counts;"
    data = pd.read_sql(query, con=engine)
    return data

if __name__