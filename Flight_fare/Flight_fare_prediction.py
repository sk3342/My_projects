import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

# Load the dataset
data = pd.read_excel("Data_Train.xlsx")

# Data Cleaning and Preprocessing
data.dropna(inplace=True)

# Convert date columns with explicit format
data['Journey_day'] = pd.to_datetime(data['Date_of_Journey'], format='%d/%m/%Y', dayfirst=True).dt.day
data['Journey_month'] = pd.to_datetime(data['Date_of_Journey'], format='%d/%m/%Y', dayfirst=True).dt.month
data['Dep_hour'] = pd.to_datetime(data['Dep_Time'], format='%I:%M %p').dt.hour
data['Dep_min'] = pd.to_datetime(data['Dep_Time'], format='%I:%M %p').dt.minute
data['Arrival_hour'] = pd.to_datetime(data['Arrival_Time'], format='%I:%M %p').dt.hour
data['Arrival_min'] = pd.to_datetime(data['Arrival_Time'], format='%I:%M %p').dt.minute

# Convert Total_Stops to numerical values
data['Total_Stops'] = data['Total_Stops'].map({
    'non-stop': 0,
    '1 stop': 1,
    '2 stops': 2,
    '3 stops': 3,
    '4 stops': 4
})

# One-hot encode categorical variables
data = pd.get_dummies(data, columns=['Airline', 'Source', 'Destination'], drop_first=True)

# Drop unnecessary columns and prepare features and target variable
X = data.drop('Price', axis=1)
y = data['Price']

# Check data types to ensure all features are numerical
print(X.dtypes)
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Model Evaluation
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
print(f"R² Score: {r2:.2f}")
print(f"Mean Squared Error: {mse:.2f}")
