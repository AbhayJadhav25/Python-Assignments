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

    feature_importance = model.feature_importances_

    maximum = ""
    minimum = ""
    imp = 0
    for cols , importance in zip(X.columns , feature_importance):
        print(cols , " " , importance)
        if(importance > imp ):
            maximum = cols
        elif(importance <= imp):
            minimum = cols

    print("Feature Contribute the most in prediction result : ",maximum , " = ",max(feature_importance))

    print("Feature Contribute less in prediction result : ",minimum , " = " ,min(feature_importance))

def main():
    trainModel()
if __name__ == "__main__":
    main()