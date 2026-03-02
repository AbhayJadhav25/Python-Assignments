import pandas as pd
from Q1 import Training
def main():
  data = {
    "StudyHours" : [6,7,3,8,4],
    "Attendance" : [85,60,90,50,75] ,
    "PreviousScore" : [78,82,55,88,60] ,
    "AssignmentsCompleted" : [7,8,6,9,5],
    "SleepHours" : [6,5,7,4,8],
    "FinalResult" : [1,0,1,0,1]
  }

  df = pd.DataFrame(data)
  df.to_csv("student5_data.csv" , index=False)
  acc_score = Training("student5_data.csv")
  print("Accuracy : ",acc_score)

if __name__ == "__main__":
  main()