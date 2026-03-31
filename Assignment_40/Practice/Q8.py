import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier , plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
def trainModel():
    df = pd.read_csv("student_performance_ml.csv")

    X = df.drop(columns=['FinalResult'])
    Y = df['FinalResult']

    X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size = 0.2 , random_state=42)

    model = DecisionTreeClassifier()

    model.fit(X_train , Y_train)
    print("Model Trained")

    #Accuracy
    Y_pred = model.predict(X_test)
    accuracy = accuracy_score(Y_pred , Y_test)
    print("Accuracy of model with all X columns = ",accuracy*100)

    plt.figure(figsize = (8,6))
    plot_tree(model , filled = True , feature_names = X.columns, class_names = ['Fail', 'Pass'])
    plt.show()
def main():
    trainModel()
if __name__ == "__main__":
    main()