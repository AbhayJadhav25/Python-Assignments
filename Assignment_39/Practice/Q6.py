import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score , confusion_matrix , classification_report

def StudentPerformance():
   border = "="*70

   df = pd.read_csv(r"D:\Marvellous\Python-Assignments\Assignment_38\student_performance_ml.csv")

   X = df.drop('FinalResult' , axis = 1)
   Y = df['FinalResult']

#    print("Shape of X = ",X.shape)
#    print("Shape of Y = ", Y.shape)

   X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size = 0.2 , random_state=42)

   model1 = DecisionTreeClassifier(max_depth=1)
   model2 = DecisionTreeClassifier(max_depth=3)
   model3 = DecisionTreeClassifier(max_depth=None)


   model1.fit(X_train , Y_train)
   model2.fit(X_train , Y_train)
   model3.fit(X_train , Y_train)

   print("Training Completed")

   Y_pred1 = model1.predict(X_test)
   Y_pred2 = model2.predict(X_test)
   Y_pred3 = model3.predict(X_test)


   accuracy1 = accuracy_score(Y_pred1 , Y_test)
   accuracy2 = accuracy_score(Y_pred2 , Y_test)
   accuracy3 = accuracy_score(Y_pred3 , Y_test)

   print("Total Accuracy with Max depth 1 = ",accuracy1*100)
   print("Total Accuracy with Max depth 3 = ",accuracy2*100)
   print("Total Accuracy with Max depth None = ",accuracy3*100)

   print("Testing Accurancy with with Max depth 1 = " ,model1.score(X_test,Y_test)*100)
   print("Testing Accurancy with with Max depth 3 = " , model2.score(X_test,Y_test)*100)
   print("Testing Accurancy with with Max depth None = " ,model3.score(X_test,Y_test)*100)

def main():
    StudentPerformance()
if __name__ == "__main__":
    main()