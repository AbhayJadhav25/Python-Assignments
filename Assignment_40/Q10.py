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
    df["PerformanceIndex"] = df["StudyHours"]*2 + df["Attendance"]

    X = df.drop("FinalResult" , axis = 1)
    Y = df["FinalResult"]

    print(X.shape)
    print(Y.shape)
    x_train , x_test , y_train , y_test = train_test_split(X,Y,test_size=0.3 , shuffle=True)

    model = DecisionTreeClassifier(max_depth= None)

    model.fit(x_train , y_train)

    Y_pred = model.predict(x_test)

    acc_score = accuracy_score(Y_pred , y_test)
    print("Accuracy : ",acc_score)

    trainging_accuracy = model.score(x_train,y_train)
    testing_accuracy = model.score(x_test , y_test)

    print("Testing Accuracy : ",testing_accuracy)
    print("Training Accuracy : ",trainging_accuracy)
def main():
  path = r"D:\Marvellous\Python-Assignments\Assignment_38\Assignment_40\student5_data.csv"
  Training(path)
if __name__ == "__main__":
  main()

#after adding the accuracy is increase in highly manner.