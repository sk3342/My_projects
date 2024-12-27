def transform_data(users, logs):
    """Transform the data by cleaning and aggregating."""
    # Example transformation: Merge users and logs
    merged_data = logs.merge(users, left_on='user_id', right_on='user_id', how='left')
    
    # Example transformation: Count actions per user
    action_counts = merged_data.groupby('username')['action'].count().reset_index()
    action_counts.columns = ['username', 'action_count']
    
    return merged_data, action_counts

if __name__ == "__main__":
    from extract import extract_data
    db_url = 'mysql+pymysql://root:password@localhost:3306/data_analysis'
    users, logs = extract_data(db_url)
    merged_data, action_counts = transform_data(users, logs)
    
    print("\nMerged Data:")
    print(merged_data)
    print("\nAction Counts:")
    print(action_counts)