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

   print(border)
   print("Question 3")
   print(border)

   accuracy = accuracy_score(Y_pred , Y_test)
   print("Total Accuracy = ",accuracy*100)

   print(border)
   print("Question 4")
   print(border)
   
   cm = confusion_matrix(Y_test , Y_pred)
   print("Confusion Matrix")
   print(cm)

   print("True Positive Value = ",cm[0][0])
   print("True Negative Value = ",cm[1][1])

   print("False Positive Value = ",cm[0][1])
   print("False Negative value = ",cm[1][0])

   print(border)
   print("Question 5")
   print(border)

   training_accuracy = model.score(X_test , Y_test)*100
   testing_accuracy = model.score(X_test , Y_test)*100

   print("Training Accuracy = ",training_accuracy)
   print("Testing Accuracy = ",testing_accuracy)

   print(border)
   print("Question 7")
   print(border)
   
   new_data = pd.DataFrame(
       [[6 ,85 , 66 , 7 ,7]]  , 
        columns= X.columns
   )
   prediction = model.predict(new_data)
   print(prediction)

   if(prediction[0]==1):
       print("pass")
   else:
       print("Fail") 
def main():
    StudentPerformance()
if __name__ == "__main__":
    main()