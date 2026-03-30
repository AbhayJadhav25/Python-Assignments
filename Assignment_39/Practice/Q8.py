import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score , confusion_matrix , classification_report
import matplotlib.pyplot as plt
def StudentPerformance():
   border = "="*70

   print(border)
   print("Step 1 : Load the datset  ")
   print("border")
   df = pd.read_csv(r"D:\Marvellous\Python-Assignments\Assignment_38\student_performance_ml.csv")

   print(border)
   print("Step 2 : Data Analysis")
   print(border)

   print("FIrst 5 Records")
   print(df.head())

   print("Last of 5 records")
   print(df.tail())

   print("Shape of Dataset = ",df.shape)
   print("Total Number of Rows = ",df.shape[0])
   print("Total Number of Columns = ",df.shape[1])

   print("Column Names")
   print(list(df.columns))

   print("Data type of Each Column")
   print(df.dtypes)
	 
   print("Statistical Report ")
   print(df.describe())
	 
   print(border)
   print("Step 3 : Visualization")
   print(border)
   
   df.hist(figsize=(8,6) , edgecolor = 'black' , color = 'skyblue')
   plt.grid(axis = 'y' ,linestyle = '--')
   plt.show()
	 
   print(border)
   print("Step 4 : Train test Split")
   print(border)
   
   X = df.drop('FinalResult' , axis = 1)
   Y = df['FinalResult']

   X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size = 0.2 , random_state=42)
	 
   print(border)
   print("Step 5 : Model Training")
   print(border)
   
   model = DecisionTreeClassifier()
   model.fit(X_train , Y_train)

   print("Training Completed")
	 
   print(border)
   print("Step 6 : Prediction")
   print(border)
   Y_pred = model.predict(X_test)
	 
   print(border)
   print("Step 7 : Accuracy Calculation")
   print(border)
	 
   accuracy = accuracy_score(Y_pred , Y_test)
   print("Total Accuracy = ",accuracy*100)
	 
   print(border)
   print("Step 8 : Confusion Matrix")
   print(border)
	 
   cm = confusion_matrix(Y_test , Y_pred)
   print("Confusion Matrix")
   print(cm)
   
   print(border)
   print("Step 9 : Final Conclusion")
   print(border)
   
   print("Train Model Accuracy = ",accuracy*100)
def main():
    StudentPerformance()
if __name__ == "__main__":
    main()