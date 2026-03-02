import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import(
  accuracy_score , 
  confusion_matrix , 
  ConfusionMatrixDisplay
)
import matplotlib.pyplot as plt
import numpy as np
def trainData(path):
  df = pd.read_csv(path)

  print(df.head())
  features = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
  ]

  X = df[features]
  y = df["FinalResult"]

  X_train , X_test , Y_train , Y_test = train_test_split(X , y , test_size = 0.2 , random_state=42)

  model = DecisionTreeClassifier(
    criterion="gini",
    random_state=42 ,
    max_depth=None
  )

  model.fit(X_train , Y_train)

  print("Model Training Complete.")
  print("Predicted Values  Actual Values")
  Y_pred = model.predict(X_test)
  for val , val2 in zip(Y_pred , Y_test.values):
    print(val,"\t\t\t", val2)

  accuracy = accuracy_score(Y_pred , Y_test)*100
  print(f"Accuracy score : {accuracy}%")

  cm = confusion_matrix(Y_test , Y_pred)
  print(cm)

  # print("True Positive Value : ",cm[0][0])
  # print("True Negative Value : ",cm[1][1])

  true_positive = np.sum((Y_pred == 0) & (Y_test == 0))
  true_Negative = np.sum((Y_pred == 1) & (Y_test == 1))

 
  print("True Positive : ",true_positive)
  print("True Negative : ",true_Negative)
  data = ConfusionMatrixDisplay(confusion_matrix = cm ,  display_labels = model.classes_)
  data.plot()
  plt.show()

  training_accuracy = model.score(X_train , Y_train)
  testing_accuracy = model.score(X_test , Y_test)

  print("Training Accuracy : ",training_accuracy*100)
  print("Tetsing Accuracy : ",testing_accuracy*100)

  new_data = pd.DataFrame([[6,85,66,7,7]] , columns=["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"])

  Y_pred = model.predict(new_data)
  if(Y_pred == [1]):
    print("Pass")
  else:
    print("Fail")


def main():
  path = r"D:\Marvellous\Python-Assignments\Assignment_38\student_performance_ml.csv"
  trainData(path)

if __name__ == "__main__":
  main()