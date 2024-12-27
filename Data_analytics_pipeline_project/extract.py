import pandas as pd
from sqlalchemy import create_engine

def extract_data(db_url):
    """Extract data from MySQL database."""
    engine = create_engine(db_url)
    users_query = "SELECT * FROM users;"
    logs_query = "SELECT * FROM network_logs;"
    
    users_data = pd.read_sql(users_query, con=engine)
    logs_data = pd.read_sql(logs_query, con=engine)
    
    return users_data, logs_data

if __name__ == "__main__":
    db_url = 'mysql+pymysql://root:password@localhost:3306/data_analysis'
    users, logs = extract_data(db_url)
    print("Users Data:")
    print(users)
    print("\nNetwork Logs Data:")
    print(logs)