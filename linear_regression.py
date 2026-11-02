import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


df = pd.DataFrame({
    "Area": [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400],
    "Price": [20, 24, 27, 33, 35, 41, 43, 49, 51, 57]
})

print("Dataset:\n", df)

X = df[["Area"]]
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

result = linregress(X_train["Area"], y_train)
slope = result.slope
intercept = result.intercept

print("\nSlope:", slope)
print("Intercept:", intercept)

y_pred = slope * X_test["Area"] + intercept

print("\nActual Prices:")
print(y_test.values)
print("\nPredicted Prices:")
print(y_pred.values.round(2))

print("\nModel Evaluation:")
print("R2 Score:", round(r2_score(y_test, y_pred), 4))
print("MAE:", round(mean_absolute_error(y_test, y_pred), 4))
print("MSE:", round(mean_squared_error(y_test, y_pred), 4))
print("RMSE:", round(np.sqrt(mean_squared_error(y_test, y_pred)), 4))

area = float(input("\nEnter house area in sq.ft.: "))
price = slope * area + intercept
print("Predicted price:", round(price, 2), "lakh")

plt.scatter(X_train["Area"], y_train, label="Training Data")
plt.scatter(X_test["Area"], y_test, label="Testing Data")
x_line = np.linspace(df["Area"].min(), df["Area"].max(), 100)
y_line = slope * x_line + intercept
plt.plot(x_line, y_line, color="red", label="Regression Line")
plt.xlabel("Area (sq.ft.)")
plt.ylabel("Price (lakh)")
plt.title("Linear Regression: House Price Prediction")
plt.legend()
plt.tight_layout()
plt.show()
