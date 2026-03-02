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
    x_train , x_test , y_train , y_test = train_test_split(X,Y,test_size=0.3 , shuffle=True ,random_state=55) #increasing the random state also increasing the Accuracy Score.

    model = DecisionTreeClassifier(max_depth= 3)

    model.fit(x_train , y_train)

    Y_pred = model.predict(x_test)

    acc_score = accuracy_score(Y_pred , y_test)

    print("Accuracy Score : ",acc_score)
    #manual accuracy_score
    
    plt.figure(figsize=(9,7))
    plot_tree(model , filled=True , feature_names=X.columns, class_names=["Fail" , "pass"])
    plt.title("Decision Tree Visualization.")
    plt.show()
def main():
  path = r"D:\Marvellous\Python-Assignments\Assignment_38\Assignment_40\student5_data.csv"
  Training(path)
if __name__ == "__main__":
  main()

  #accuracy = 0.4