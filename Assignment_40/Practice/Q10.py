import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier , plot_tree
from sklearn.metrics import accuracy_score
def trainModel():
    df = pd.read_csv("student_performance_ml.csv")
    df['Performance'] = df['StudyHours']*2 + df['Attendance']
    X = df.drop(columns=['FinalResult'])
    Y = df['FinalResult']

    print(X.shape)
    X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size = 0.3 , random_state=42)

    model = DecisionTreeClassifier(max_depth=3)

    model.fit(X_train , Y_train)
    print("Model Trained")

    #Training Accuracy
    Y_train_pred = model.predict(X_train)
    train_acc = accuracy_score(Y_train , Y_train_pred)
    print("Training accuracy = ",train_acc*100) 

    #Testing Accuracy
    Y_test_pred = model.predict(X_test)
    test_acc = accuracy_score(Y_test , Y_test_pred)
    print(f"Testing accuracy = {test_acc*100:.2f}%")

def main():
    trainModel()
if __name__ == "__main__":
    main()