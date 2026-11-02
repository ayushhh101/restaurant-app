import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, ConfusionMatrixDisplay, classification_report
)


df = pd.DataFrame({
    "StudyHours": [1, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8],
    "Result": [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
})

print("Dataset:\n", df)


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


z = np.linspace(-10, 10, 100)
plt.plot(z, sigmoid(z))
plt.xlabel("z")
plt.ylabel("Sigmoid(z)")
plt.title("Sigmoid Function")
plt.grid()
plt.tight_layout()
plt.show()

X = df[["StudyHours"]]
y = df["Result"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("\nActual Results:")
print(y_test.values)
print("\nPredicted Results:")
print(y_pred)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)

cm = confusion_matrix(y_test, y_pred, labels=[0, 1])
print("\nConfusion Matrix:")
print(cm)

print("\nClassification Report:")
print(classification_report(
    y_test, y_pred, labels=[0, 1],
    target_names=["Fail", "Pass"], zero_division=0
))

hours = float(input("\nEnter study hours: "))
new_student = pd.DataFrame({"StudyHours": [hours]})
prediction = model.predict(new_student)
probability = model.predict_proba(new_student)

print("Predicted Result (0=Fail, 1=Pass):", prediction[0])
print("Probability of Fail:", round(probability[0][0] * 100, 2), "%")
print("Probability of Pass:", round(probability[0][1] * 100, 2), "%")

plt.scatter(X_train["StudyHours"], y_train, label="Training Data")
plt.scatter(X_test["StudyHours"], y_test, label="Actual Test Data")
plt.scatter(
    X_test["StudyHours"], model.predict_proba(X_test)[:, 1],
    label="Predicted Probability"
)
plt.xlabel("Study Hours")
plt.ylabel("Result / Probability")
plt.title("Logistic Regression")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

ConfusionMatrixDisplay.from_predictions(
    y_test, y_pred, labels=[0, 1],
    display_labels=["Fail", "Pass"], cmap="Blues"
)
plt.title("Logistic Regression Confusion Matrix")
plt.tight_layout()
plt.show()

metrics = {
    "Accuracy": accuracy,
    "Precision": precision,
    "Recall": recall,
    "F1 Score": f1
}

plt.bar(metrics.keys(), metrics.values())
plt.xlabel("Evaluation Metrics")
plt.ylabel("Score")
plt.title("Logistic Regression Performance")
plt.ylim(0, 1)
plt.grid(axis="y")
plt.tight_layout()
plt.show()
