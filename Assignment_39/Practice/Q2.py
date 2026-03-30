import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score , confusion_matrix , classification_report

def StudentPerformance():
   border = "="*70
   print(border)
   print("Question 1")
   print(border)

   df = pd.read_csv(r"D:\Marvellous\Python-Assignments\Assignment_38\student_performance_ml.csv")

   X = df.drop('FinalResult' , axis = 1)
   Y = df['FinalResult']

#    print("Shape of X = ",X.shape)
#    print("Shape of Y = ", Y.shape)

   X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size = 0.2 , random_state=42)

   model = DecisionTreeClassifier()
   model.fit(X_train , Y_train)

   print("Training Completed")

   print(border)
   print("Question 2")
   print(border)

   print("Actual Values","","Predicted Values")
   Y_pred = model.predict(X_test)
   for actual , pred in zip(Y_pred , Y_test):
       print(actual , "\t\t\t",pred)
   
def main():
    StudentPerformance()
if __name__ == "__main__":
    main()