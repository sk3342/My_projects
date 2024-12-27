import mysql.connector
import pandas as pd

# Connect to the database
def create_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',  # replace with your MySQL username
        password='password',  # replace with your MySQL password
        database='data_analysis'  # use your database name here
    )
    return connection

# Fetch data from the database
def fetch_data():
    connection = create_connection()
    query = """
    SELECT u.username, nl.timestamp, nl.action 
    FROM users u 
    JOIN network_logs nl ON u.user_id = nl.user_id;
    """
    df = pd.read_sql(query, connection)
    connection.close()
    return df

# Main function
if __name__ == "__main__":
    data = fetch_data()
    print(data)