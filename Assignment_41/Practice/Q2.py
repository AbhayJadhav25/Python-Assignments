import pandas as pd
import math

def EuclideanDistance(data , new_point):
    ans = math.sqrt(((data['X'] - new_point['X'])**2)+(data['Y'] - new_point['Y'])**2)
    return ans
def k_neighbour(sorted_data , k):
    # k = int(input("Enter K neighbour : "))

    nearest = sorted_data[:k]
    print(nearest)
    votes = {}

    for i in range(len(nearest)):
        row = nearest.iloc[i]
        label = row['Label']

        if label in votes:
            votes[label] +=1
        else:
            votes[label] = 1

    ans = max(votes , key = votes.get)
    print(f"Predicted output is {ans} when k = {k}")


def main():
    data = {
        "Point" : ['A' , 'B' , 'C' , 'D' ] ,
        "X" : [1,2,3,4] ,
        "Y" : [2,3,1,5] , 
        "Label" : ["Red" , "Red" , "Blue" , "Blue"]
    }

    data = pd.DataFrame(data)

    X = int(input("Enter X-coordinates = "))
    Y = int(input("Enter y-coordinates = "))

    new_point = {'X' : X , 'Y' : Y}

    for i in range(len(data)):
        data.loc[i , 'distance'] = EuclideanDistance(data.iloc[i] , new_point)

    sorted = data.sort_values(by='distance')

    k_neighbour(sorted , 1)
    k_neighbour(sorted , 3)
    k_neighbour(sorted , 5)


if __name__ == "__main__":
    main()