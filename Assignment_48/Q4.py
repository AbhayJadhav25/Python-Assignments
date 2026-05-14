import numpy as np
from sklearn.preprocessing import StandardScaler

def EuclideanDistance(p1 , p2):
    ans = np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) 

    return ans
def afterScaling(p1,p2):
    scaler = StandardScaler()
    
    data = [p1 , p2]
    scaled_data = scaler.fit_transform(data)
    ans = EuclideanDistance(scaled_data[0] , scaled_data[1])

    return ans 

def beforeScaling(p1 , p2):
    ans = EuclideanDistance(p1,p2)
    return ans

def main():
    p1 = [20 , 45]
    p2 = [18 , 47]

    ans = beforeScaling(p1,p2)
    print(f"Euclidean Distance Before Scaling  =  {ans}") #2.8284271247461903


    ans = afterScaling(p1,p2)
    print(f"Euclidean Distance after Scaling  =  {ans}") #2.8284271247461903

if __name__ == "__main__":
    main()

'''
Euclidean Distance is remains same before and after scaling
'''