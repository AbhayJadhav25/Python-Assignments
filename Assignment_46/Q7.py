import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def trainModel():
    data = pd.DataFrame({
        'study_hours' : [1,2,3,4,5] , 
        'Marks' : [55,55,60,65,70]
    })

    X = data[['study_hours']]
    Y = data['Marks']



    model = LinearRegression()

    model.fit(X,Y)

    print("Coefficient = ",model.coef_)
    print("Intercept  =  ",model.intercept_)

    return model

if __name__ == "__main__":
    main()