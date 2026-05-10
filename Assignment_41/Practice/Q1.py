import pandas as pd
import math
def EuclideanDist(new_point , data):
    ans =  math.sqrt(((new_point['X'] - data['X'])**2) + ((new_point['Y']-data['Y'])**2))
    return ans
def userdefinedKNN():
    data = {
        "Point" : ['A','B','C','D'],
        'X' : [1,2,3,4] ,
        'Y' : [2,3,1,5] ,
        'Label' : ['Red' , 'Red' , 'Blue' ,'Blue']
    }

    df = pd.DataFrame(data)
    
    print("Enter new Coordinates of X and Y :")
    X = int(input("Enter X coordinate = "))
    Y = int(input("Enter X coordinate = "))

    new_point = {'X' : X , 'Y' : Y}

    for i in range(len(df)):
        df.loc[i , 'Distance'] = EuclideanDist(df.iloc[i] , new_point)   #df.loc[i , 'Distance'] --> distance column of ith row

    sorted_data = df.sort_values(by='Distance')
    print(sorted_data)
    
    k = 3
    nearest = sorted_data[:3]
    print(nearest)

    votes = {}
    for i in range(len(nearest)):
        row = nearest.iloc[i]
        label = row['Label']

        if label in votes:
            votes[label]+=1
        else:
            votes[label] =1
    print(votes) 

    ans = max(votes , key = votes.get)
    print("Final Prediction is = ",ans)

def main():
    userdefinedKNN()
if __name__ == "__main__":
    main()