import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier , plot_tree
import matplotlib.pyplot as plt
import seaborn as sna
from sklearn.metrics import accuracy_score
import numpy as np
def Training2(path , colName = None):
    df = pd.read_csv(path)
    print(df.head())  #data loaded Successfully.
    df = df.drop(colName , axis=1)
    print(df.head()) 
    features_cols = [
       "StudyHours", "Attendance" , "PreviousScore" , 
       "AssignmentsCompleted"
    ]

    X = df.drop("FinalResult" ,axis = 1)
    Y = df["FinalResult"]

    print(X.shape)
    print(Y.shape)
    x_train , x_test , y_train , y_test = train_test_split(X,Y,test_size=0.3 , random_state = 12 , shuffle=True)

    model = DecisionTreeClassifier(max_depth= 3)

    model.fit(x_train , y_train)

    Y_pred = model.predict(x_test)

    acc_score = accuracy_score(Y_pred , y_test)
    print("Accuracy Score : ",acc_score)

    return acc_score
def main():
  path = r"D:\Marvellous\Python-Assignments\Assignment_38\Assignment_40\student_performance_ml.csv"

  colname = "SleepHours"

  Training(path , colname)
if __name__ == "__main__":
  main()