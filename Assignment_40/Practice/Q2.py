import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
def trainModel():
    df = pd.read_csv("student_performance_ml.csv")

    X = df.drop(columns=['FinalResult'])
    Y = df['FinalResult']

    print("Shape of X = ",X.shape)
    print("Shape of Y = ",Y.shape)

    X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size = 0.2 , random_state=42)

    model = DecisionTreeClassifier()

    model.fit(X_train , Y_train)
    print("Model Trained")

    #Accuracy
    Y_pred = model.predict(X_test)
    accuracy_old = accuracy_score(Y_pred , Y_test)
    print("Accuracy of model with all X columns = ",accuracy_old*100)

    X = df.drop(columns=['SleepHours' , 'FinalResult'])
    Y = df['FinalResult']

    X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    model.fit(X_train , Y_train)
    Y_pred = model.predict(X_test)
    accuracy_new = accuracy_score(Y_pred , Y_test)

    print("Accuracy after dropping column  Sleephours = ",accuracy_old*100)

    if(accuracy_new == accuracy_old):
        print("NO affect")
    elif(accuracy_old>accuracy_new):
        print("Accuracy with all columns is high")
    else:
        print("Accuracy after drop the column is high")
def main():
    trainModel()
if __name__ == "__main__":
    main()