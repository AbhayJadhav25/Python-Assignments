from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
def trainModel(data):
    X = data.drop('Salary' , axis =1)
    Y = data['Salary']

    model = LinearRegression()

    model.fit(X,Y)
    new_data = pd.DataFrame([[6]] , columns=['Experience'])
    predict_salary = model.predict(new_data)
    print(f"Precicted Salary = {predict_salary[0]:.2f}")

    plt.scatter(X , Y , color = 'blue' , label = 'Data Points')
    plt.plot(X , model.predict(X) , color = 'red' , label = "Regression Line")

    plt.xlabel("Experience(Years)")
    plt.ylabel("Salary")
    plt.title("Experience vs Salary Regression")
    plt.legend()
    plt.show()
    
def main():
    data = {
        "Experience" : [1,2,3,4,5],
        "Salary" : [20000 , 25000 , 30000 , 35000 , 40000]
    }

    data = pd.DataFrame(data)
    trainModel(data)
if __name__ == "__main__":
    main()