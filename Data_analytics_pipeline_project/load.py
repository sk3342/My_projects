from sqlalchemy import create_engine

def load_data(action_counts, db_url):
    """Load action counts into MySQL database."""
    engine = create_engine(db_url)
    action_counts.to_sql('action_counts', con=engine, if_exists='replace', index=False)

if __name__ == "__main__":
    from transform import transform_data
    from extract import extract_data
    
    db_url = 'mysql+pymysql://root:password@localhost:3306/data_analysis'
    users, logs = extract_data(db_url)
    merged_data, action_counts = transform_data(users, logs)
    load_data(action_counts, db_url)
    print("\nAction counts loaded into the database.")