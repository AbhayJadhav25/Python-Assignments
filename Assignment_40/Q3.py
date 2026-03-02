from Q1 import Training
from Q2 import Training2
def main():
  path = r"D:\Marvellous\Python-Assignments\Assignment_38\student_performance_ml.csv"

  path2 = r"D:\Marvellous\Python-Assignments\Assignment_38\Assignment_40\student_performance_ml.csv"
  
  cols = ["StudyHours" ,"Attendance"]
 
  full_feature_model = Training(path)
  half_feature_model = Training2(path2 , cols)

  print(full_feature_model)
  print(half_feature_model)

  if(full_feature_model == half_feature_model):
    print(f"After removes {cols} model still perfoeming well")
  elif(full_feature_model > half_feature_model):
    print(f"After removes {cols} full_feature_model still perfoeming well")
  else:
    print(f"After removes {cols} Half_feature_model still perfoeming well")

if __name__ == "__main__":
  main()