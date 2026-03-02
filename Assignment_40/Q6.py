import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier , plot_tree
import matplotlib.pyplot as plt
import seaborn as sna
from sklearn.metrics import accuracy_score
import numpy as np
from Q2 import Training2
def Training(path):
    df = pd.read_csv(path)
    # print(df.head())  #data loaded Successfully.

    features_cols = [
       "StudyHours", "Attendance" , "PreviousScore" , 
       "AssignmentsCompleted" , "SleepHours"
    ]

    X = df[features_cols]
    Y = df["FinalResult"]

    print(X.shape)
    print(Y.shape)
    x_train , x_test , y_train , y_test = train_test_split(X,Y,test_size=0.3 , shuffle=True)

    model = DecisionTreeClassifier(max_depth= 3)

    model.fit(x_train , y_train)

    Y_pred = model.predict(x_test)

    acc_score = accuracy_score(Y_pred , y_test)


    #manual accuracy_score
    False_values = 0
    for i in range(len(Y_pred)):
      if(not(Y_pred[i] == y_test.iloc[i] == 0)):
        print(list(x_test.iloc[i]))
        False_values+=1

    print("Misclassified Students : ",False_values)
def main():
  path = r"D:\Marvellous\Python-Assignments\Assignment_38\Assignment_40\student5_data.csv"
  Training(path)
if __name__ == "__main__":
  main()