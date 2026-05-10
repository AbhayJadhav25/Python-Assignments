
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
def main():
    x = [1,2,3,4,5]
    y = [3,4,2,4,5]

    x_mean = mean(x)
    y_mean = mean(y)

    slope_m = slope(x , y , x_mean , y_mean)

    intercept_b = intercept(y_mean , slope_m , x_mean)

    print(f"X_mean = {x_mean:.2f}")
    print(f"Y_mean = {y_mean:.2f}")
    print(f"Slope = {slope_m:.2f}")
    print(f"intercept = {intercept_b:.2f}")


if __name__ == "__main__":
    main()