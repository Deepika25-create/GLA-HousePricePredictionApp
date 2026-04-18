import pandas as pd
from sklearn.linear_model import LinearRegression

import joblib

data = pd.read_csv("house_data.csv")

X = data[['Size', 'Bedrooms','Age']]

y = data['Price']

model = LinearRegression()

model.fit(X, y)

joblib.dump(model, "house_model.pkl")
print("Model trained and saved successfully")

