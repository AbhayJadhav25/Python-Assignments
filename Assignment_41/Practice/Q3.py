import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def predict(data):
    X = data.drop('Result' , axis = 1)
    Y = data['Result']

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X , Y)
    new_data = pd.DataFrame([[4 , 70]] , columns=['Study_Hours' , 'Attendance'])
    prediction = model.predict(new_data)
    print(f"Prediction : ",prediction[0])

    '''
    In these we not split the dataset into train ,test it gives wrong prediction because our data set is too small.
    '''
def main():
    study_hours = []
    attendance = []
    result = []

    # for i in range(4):
    #     print(f"Enter Study Hours , attendance , result of student {i}")
    #     study_hour = int(input("Study Hour = "))
    #     attend  = int(input("Attendance = "))
    #     res = input("Enter result = ")

    #     study_hours.append(study_hour)
    #     attendance.append(attend)
    #     result.append(res)

    data = {
        "Study_Hours" :[2,5,6,1] ,
        "Attendance" : [60,80,85,50] , 
        "Result" : ['Fail' , 'Pass' , 'Pass' , 'Fail']
    }

    data = pd.DataFrame(data)

    predict(data)
    
if __name__ == "__main__":
    main()