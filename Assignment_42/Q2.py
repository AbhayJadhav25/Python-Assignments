
def mean(X):
    sum = 0
    for i in range(len(X)):
        sum = sum + X[i]
    
    return sum/len(X)
def intercept(y_mean , slope , x_mean):
    return y_mean - slope*x_mean

def slope(x , y , x_mean , y_mean):
    numerator = 0
    denominator = 0

    for i , j in zip(x , y):
        numerator = numerator + ((i - x_mean) *(j - y_mean))

        denominator = denominator + ((i - x_mean)**2)

    m = numerator/denominator

    return m 

def predictedValues(slope , x , intercept):
    y_pred = []
    for i in range(len(x)):
        pred = slope*x[i] + intercept
        y_pred.append(pred)

    return y_pred

def mse(y , y_pred):
    total_error = 0
    for i in range(len(y)):
        total_error = total_error + ((y[i]-y_pred[i])**2)

    return total_error / len(y)

def r_squared(y,y_pred , y_mean):
    '''
    formula : 1 - (SSres / SStotal)
    '''
    numerator = 0
    denominator = 0

    for i in range(len(y)):
        numerator = numerator + ((y[i] - y_pred[i])**2)
        denominator = denominator + ((y[i] - y_mean)**2)

    return 1 - (numerator / denominator)

def main():
    x = [1,2,3,4,5]
    y = [3,4,2,4,5]

    x_mean = mean(x)
    y_mean = mean(y)

    slope_m = slope(x , y , x_mean , y_mean)

    intercept_b = intercept(y_mean , slope_m , x_mean)

    y_pred = predictedValues(slope_m , x , intercept_b)

    mean_squared_error = mse(y , y_pred)

    r_square = r_squared(y,y_pred , y_mean)

    print(f"Predicted Values : {y_pred}")
    print(f"Mean Squared Error : {mean_squared_error:.2f}")
    print(f"R_squared = {r_square:.2f}")

if __name__ == "__main__":
    main()