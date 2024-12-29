import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve

# Step 1: Load the dataset
data = pd.read_csv('/Users/sriramkoyalkar/Desktop/My_projects/Employee_attrition/employee_attrition.csv')

# Step 2: Data Understanding
print(data.head())
print(data.info())
print(data.describe())

# Step 3: Data Preprocessing
# Handle missing values
data = data.dropna()

# Encode categorical variables
encoder = LabelEncoder()
data['Attrition'] = encoder.fit_transform(data['Attrition'])
data = pd.get_dummies(data, drop_first=True)

# Feature scaling
scaler = StandardScaler()
features = data.drop('Attrition', axis=1)
labels = data['Attrition']
scaled_features = scaler.fit_transform(features)

# Step 4: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(scaled_features, labels, test_size=0.3, random_state=42)

# Step 5: Model Building - Random Forest
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Step 6: Model Evaluation
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]

print("Classification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

roc_auc = roc_auc_score(y_test, y_proba)
print(f"ROC-AUC Score: {roc_auc}")

# ROC Curve
fpr, tpr, _ = roc_curve(y_test, y_proba)
plt.plot(fpr, tpr, label=f"ROC Curve (AUC = {roc_auc:.2f})")
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()

# Step 7: Save the Model

import joblib
joblib.dump(model, 'employee_attrition_model.pkl')

print("Model saved as employee_attrition_model.pkl")
