import pandas as pd
import numpy as np
import math

def EucDistance(data , new_point):
  ans = math.sqrt((new_point['X'] - data['X'])**2 + (new_point['Y'] - data['Y'])**2)
  return ans

def EuclideanDistance(Data):
  for i in Data:
    print(i)
  X_coordinate = int(input("Enter X coordinates : "))
  Y_coordinate = int(input("Enter Y coordinates : "))

  new_point = {'X' : X_coordinate , 'Y' : Y_coordinate}

  for i in Data:
    i['distance'] = EucDistance(i , new_point)
  
  for i in Data:
    print(i)

  sorted_data = sorted(Data , key = lambda item : item['distance'])

  for i in sorted_data:
    print(i)

  k = 3
  nearest = sorted_data[:k]

  for d in nearest:
    print(d)
  
  votes = {}
  for neighbour in nearest : 
    label = neighbour['label']
    votes[label] = votes.get(label , 0)+1

  for d in votes : 
    print("Name : ",d,"Number of votes : ",votes[d])
  
  predict = max(votes , key = votes.get)

  print(f"Predicted class of ({X_coordinate , Y_coordinate}) is {predict}")

def main():
  data =[
    {'Point' : 'A' , 'X' : 1 , 'Y' : 2 , 'label' : 'Red'},
    {'Point' : 'B' , 'X' : 2 , 'Y' : 1 , 'label' : 'Red'},
    {'Point' : 'C' , 'X' : 3 , 'Y' : 3 , 'label' : 'Blue'},
    {'Point' : 'D' , 'X' : 4 , 'Y' : 5 , 'label' : 'Blue'},
  ]

  EuclideanDistance(data)
if __name__ == "__main__":
  main()