import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay


df = pd.DataFrame({
    "StudyHours": [1, 2, 2, 3, 3, 4, 5, 6, 7, 8],
    "Attendance": [40, 45, 50, 50, 55, 65, 70, 75, 85, 90],
    "Result": [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
})

print("Dataset:\n", df)

X = df[["StudyHours", "Attendance"]]
y = df["Result"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

svm = Pipeline([
    ("scaler", StandardScaler()),
    ("svc", SVC(kernel="linear"))
])
svm.fit(X_train, y_train)
y_pred = svm.predict(X_test)

print("\nBasic SVM Accuracy:", accuracy_score(y_test, y_pred))
print("Basic SVM Confusion Matrix:\n", confusion_matrix(y_test, y_pred, labels=[0, 1]))

ConfusionMatrixDisplay.from_predictions(
    y_test, y_pred, labels=[0, 1], display_labels=["Fail", "Pass"]
)
plt.title("Basic SVM Confusion Matrix")
plt.tight_layout()
plt.show()

param_grid = {
    "svc__C": [0.1, 1, 10],
    "svc__kernel": ["linear", "rbf", "poly"]
}

grid = GridSearchCV(
    Pipeline([
        ("scaler", StandardScaler()),
        ("svc", SVC())
    ]),
    param_grid,
    cv=3,
    scoring="accuracy"
)

grid.fit(X_train, y_train)
best_model = grid.best_estimator_
grid_pred = best_model.predict(X_test)

print("\nBest Parameters:", grid.best_params_)
print("GridSearchCV SVM Accuracy:", accuracy_score(y_test, grid_pred))
print("GridSearchCV Confusion Matrix:\n", confusion_matrix(y_test, grid_pred, labels=[0, 1]))

ConfusionMatrixDisplay.from_predictions(
    y_test, grid_pred, labels=[0, 1], display_labels=["Fail", "Pass"]
)
plt.title("GridSearchCV SVM Confusion Matrix")
plt.tight_layout()
plt.show()

comparison = pd.DataFrame({
    "Model": ["Basic SVM", "SVM with GridSearchCV"],
    "Accuracy": [
        accuracy_score(y_test, y_pred),
        accuracy_score(y_test, grid_pred)
    ]
})

print("\nModel Comparison:\n", comparison)
