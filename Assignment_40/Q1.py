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
    # print("Accuracy Score : ",acc_score)

    # importances = model.feature_importances_
    # print(importances)
    # for feature , importance in zip(features_cols , importances):
    #    print(f"{feature} importance = {importance}")

    # plt.figure(figsize=(8,6))
    # plot_tree(model, feature_names=X.columns, filled=True) #we can see Decision tree use only one feature to predict the output.
    # plt.show()

    #Higher Contribution and less contributon
    # data = {
    #    "features": features_cols,
    #    "Important" :importances
    # }

    # dobj = pd.DataFrame(data)
    # print(dobj)
    # sorted_df =dobj.sort_values(by="Important" , ascending=False)

    # print("Most Contribute Feature : \n" , sorted_df.iloc[0])
    # print("Least Contribute Features :\n ",sorted_df.iloc[-1])

    # acc_score2 = Training2("D:\Marvellous\Python-Assignments\Assignment_38\Assignment_40\student_performance_ml.csv" , "SleepHours")

    # Difference = abs(acc_score - acc_score2)
    # print("Difference Between Two Accuracy : ",Difference)

    #manual accuracy_score
    TP = 0 
    TN= 0 
    FP = 0 
    FN=0
    for i in range(len(Y_pred)):
      if(Y_pred[i]==1 and y_test.iloc[i]==1):
        TP+=1
      elif(Y_pred[i] == 0 and y_test.iloc[i]==0):
        TN+=1
      elif(Y_pred[i]==1 and y_test.iloc[i] == 0):
        FP+=1
      else:
        FP+=1
    return acc_score , TP , TN , FP , FN
def main():
  path = r"D:\Marvellous\Python-Assignments\Assignment_38\student_performance_ml.csv"
  Training(path)
if __name__ == "__main__":
  main()