import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error


df = pd.DataFrame({
    "Area": [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400],
    "Bedrooms": [1, 1, 2, 2, 2, 3, 3, 3, 4, 4],
    "Age": [10, 8, 10, 8, 6, 8, 6, 4, 6, 4],
    "Location": ["A", "B", "A", "B", "A", "B", "A", "B", "A", "B"],
    "Price": [20, 24, 28, 32, 36, 40, 44, 48, 52, 56]
})

print("Dataset:\n", df)

df = pd.get_dummies(df, columns=["Location"], drop_first=True, dtype=int)
X = df.drop("Price", axis=1)
y = df["Price"]
X = X[["Area", "Bedrooms", "Age", "Location_B"]]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),
    ("regression", LinearRegression())
])
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

predictions = pd.DataFrame({
    "Actual Price": y_test.values,
    "Predicted Price": y_pred.round(2)
})

print("\nPredictions:\n", predictions)
print("\nR2 Score:", r2_score(y_test, y_pred))
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.named_steps["regression"].coef_
})

print("\nRegression Coefficients:\n", coefficients)
print("Intercept:", model.named_steps["regression"].intercept_)
