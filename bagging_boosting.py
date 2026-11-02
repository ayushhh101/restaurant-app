import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


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

models = {
    "Decision Tree (Gini)": DecisionTreeClassifier(
        criterion="gini", random_state=42
    ),
    "AdaBoost (Boosting)": AdaBoostClassifier(
        n_estimators=10, random_state=42
    ),
    "Random Forest (Bagging)": RandomForestClassifier(
        n_estimators=10, criterion="gini", random_state=42
    )
}

results = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred, labels=[0, 1])
    results[name] = accuracy

    print("\n", name)
    print("Accuracy:", round(accuracy * 100, 2), "%")
    print("Confusion Matrix:\n", cm)
    print("Predictions:", y_pred)

    plt.figure(figsize=(5, 4))
    sns.heatmap(
        cm, annot=True, fmt="d", cmap="Blues",
        xticklabels=["Fail (0)", "Pass (1)"],
        yticklabels=["Fail (0)", "Pass (1)"]
    )
    plt.title(name + " - Confusion Matrix")
    plt.xlabel("Predicted Result")
    plt.ylabel("Actual Result")
    plt.tight_layout()
    plt.show()

comparison = pd.DataFrame({
    "Model": list(results.keys()),
    "Accuracy (%)": [round(value * 100, 2) for value in results.values()]
})

print("\nAccuracy Comparison:")
print(comparison.to_string(index=False))

plt.figure(figsize=(8, 5))
plt.bar(comparison["Model"], comparison["Accuracy (%)"])
plt.title("Model Accuracy Comparison")
plt.xlabel("Machine Learning Model")
plt.ylabel("Accuracy (%)")
plt.ylim(0, 100)
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()
