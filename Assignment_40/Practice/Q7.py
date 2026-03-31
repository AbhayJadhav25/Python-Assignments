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

    model1 = DecisionTreeClassifier(random_state=0)
    model2 = DecisionTreeClassifier(random_state=10)
    model3 = DecisionTreeClassifier(random_state=42)

    model1.fit(X_train , Y_train)
    model2.fit(X_train , Y_train)
    model3.fit(X_train , Y_train)
    print("Model Trained")

    test_accuracy1 = model1.score(X_test , Y_test)
    test_accuracy2 = model2.score(X_test , Y_test)
    test_accuracy3 = model3.score(X_test , Y_test)

    Y_pred1 = model1.predict(X_test)
    Y_pred2 = model2.predict(X_test)
    Y_pred3 = model3.predict(X_test)

    acuracy1 = accuracy_score(Y_pred1 , Y_test)
    acuracy2 = accuracy_score(Y_pred2 , Y_test)
    acuracy3 = accuracy_score(Y_pred3 , Y_test)

    print("Testing Accuracy with Random state 0 = ",test_accuracy1)
    print("Accuracy with Random state 0 = ",acuracy1)
    print("Testing Accuracy with Random state 10 = ",test_accuracy2)
    print("Accuracy with Random state 0 = ",acuracy2)
    print("Testing Accuracy with Random state 42 = ",test_accuracy3)
    print("Accuracy with Random state 0 = ",acuracy3)

def main():
    trainModel()
if __name__ == "__main__":
    main()