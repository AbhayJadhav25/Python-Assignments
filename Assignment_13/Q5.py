def DisplayGrade(Mark1 ,Mark2,Mark3):
  Percentage = (Mark1+Mark2+Mark3)/3

  Grade = "Distincation" if Percentage > 75 else "First Class" if Percentage > 60 else "Second Class" if Percentage > 50 else "Fail"

  return Grade
def main():
  print("Enter Marks of Three Subjects: ")
  Mark1 = int(input())
  Mark2 = int(input())
  Mark3 = int(input())

  Res = DisplayGrade(Mark1 ,Mark2,Mark3)
  print("Grade = ",Res)
  
if __name__ == "__main__" :
  main()