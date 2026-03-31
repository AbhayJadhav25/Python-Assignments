import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
def StudentDF():

    df = pd.read_csv("student_performance_ml.csv")

    X = df.drop(columns=['FinalResult'])
    Y = df['FinalResult']

    X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size = 0.2 , random_state=42)

    model = DecisionTreeClassifier()

    model.fit(X_train , Y_train)
    print("Model Trained")
    
    new_Data = pd.DataFrame([
        {'StudyHours' : 9.0 , 'Attendance':80 , 'PreviousScore' : 72 , 'AssignmentsCompleted' : 4 , 'SleepHours' : 7 },
        {'StudyHours' : 4.0 , 'Attendance':55 , 'PreviousScore' : 58 , 'AssignmentsCompleted' : 3 , 'SleepHours' : 8},
        {'StudyHours' : 5 , 'Attendance':90 , 'PreviousScore' : 64 , 'AssignmentsCompleted' : 4 , 'SleepHours' : 4},
        {'StudyHours' : 2 , 'Attendance':60 , 'PreviousScore' : 71 , 'AssignmentsCompleted' : 5 , 'SleepHours' : 5},
        {'StudyHours' : 1 , 'Attendance':50 , 'PreviousScore' : 52 , 'AssignmentsCompleted' : 4 , 'SleepHours' : 6},
    ])

    Y_pred = model.predict(new_Data)
    new_Data["Result"] = model.predict(new_Data)
    print(Y_pred)
    print(new_Data)
def main():
    StudentDF()
if __name__ == "__main__":
    main()