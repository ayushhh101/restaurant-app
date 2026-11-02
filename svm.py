import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
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

model = make_pipeline(StandardScaler(), SVC(kernel="linear"))
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("\nPredictions:", y_pred)
print("Actual Values:", y_test.values)
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred, labels=[0, 1]))

ConfusionMatrixDisplay.from_predictions(
    y_test, y_pred, labels=[0, 1],
    display_labels=["Fail", "Pass"], cmap="Blues"
)
plt.title("SVM Confusion Matrix")
plt.tight_layout()
plt.show()

hours = float(input("\nEnter Study Hours: "))
attendance = float(input("Enter Attendance (%): "))
new_student = pd.DataFrame({
    "StudyHours": [hours],
    "Attendance": [attendance]
})
prediction = model.predict(new_student)

if prediction[0] == 1:
    print("Predicted Result: Pass")
else:
    print("Predicted Result: Fail")
