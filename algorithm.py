import pandas as pd
import numpy as np
import seaborn as sns
import sklearn
import joblib


# Load and store the data into a variable
df = pd.read_csv('heart.csv')


# Splitting the data for training and testing, X is features and Y is target variable
# X -- train _X, test_X 80/20
# Y -- train_Y, test_Y

X = df.drop('target', axis=1)
Y = df['target']

#Again, split the data into 80% for training and 20% for testing dataset
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=1)


# Feature Scaling the values in the data to be values between 0 and 1

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()


X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# Training 
# [Using ML algorithm], Random Forest 
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()

rf.fit(X_train, Y_train)

Y_pred = rf.predict(X_test)

from sklearn.metrics import accuracy_score
acc_rf = accuracy_score(Y_test, Y_pred)

print(acc_rf*100,'%')


filename = 'heart.sav'
joblib.dump(rf, filename)