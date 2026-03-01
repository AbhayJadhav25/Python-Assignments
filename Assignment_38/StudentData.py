import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import(
  accuracy_score ,
  confusion_matrix,
  classification_report ,
  ConfusionMatrixDisplay
)

#Step 1 : Load the Data
Dataset = r"D:\Marvellous\Python-Assignments\Assignment_38\student_performance_ml.csv"
df = pd.read_csv(Dataset)
print("Dataset load successfully")
print("Initial Entry from Dataset ")
print(df.head())
print("Last 5 Record : ")
print(df.tail())

print("Data Types of Each Column : ")
print(df.dtypes)
print("*"*10,"Step 1 Completed","*"*10)

#step 2 
total_stud = df.shape[0]
print("Total Number of students in Dataset : ",df.shape[0])
pass_count = df["FinalResult"].value_counts().get(1,0)
print("Total number of Passed Students  : ",pass_count)
fail_count = df["FinalResult"].value_counts().get(0,0)
print("Total number of Passed Students  : ",fail_count)

print("*"*10,"Step 2 Completed","*"*10)

#step 3 :
import math
total_hour = sum(df["StudyHours"])
print("Average of Study Hour : ",total_hour / total_stud)
print("Average Attendance : ",sum(df["Attendance"]) / total_stud)
print("Maximum Previous Score : ", max(df["PreviousScore"]))
print("Minimum Sleep Scores : ", min(df["SleepHours"]))

print("*"*10,"Step 3 Completed","*"*10)

#step 4 :
result_distribution = df["FinalResult"].value_counts()
print("Result Distribution : \n")
print(result_distribution)

print("Average of pass student : ", (pass_count/df.shape[0])*100)
print("Average of Fail student : ", (fail_count/df.shape[0])*100)

print("*"*10,"Step 4 Completed","*"*10)
#step 5 : 
""" previous number > 55 , attendance more than nearly 75% , study_hours time >= 5 that all factors increase the chances of pasiing.""" 
print("*"*10,"Step 5 Completed","*"*10)

#step 6 :Histogram of study Hours
plt.figure(figsize = (8,5))
plt.hist(df["SleepHours"] , color = "skyblue" , edgecolor = "black")
plt.title("Sleeping Hours Histogram")
plt.xlabel("Sleeping Hours")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

""""9 students take sleep of 8 hours ,most of the students take sleep of 6-7 hours is that 16 students.only 5 students take sleep of 5 hours."""
print("*"*10,"Step 6 Completed","*"*10)

plt.figure(figsize=(8,5))

sns.scatterplot(data=df,
                x="StudyHours",
                y="PreviousScore",
                hue = "FinalResult" , 
                palette = {
                  1 : "green" ,
                  0 : "red"
                }
                )

plt.grid(True)
plt.legend() 
plt.show()

#Manually
pass_student = df[df["FinalResult"]==1]
fail_student = df[df["FinalResult"]==0]

sns.scatterplot(x = pass_student["StudyHours"] , 
                y =pass_student["PreviousScore"] ,
                color = "green" ,
                label = "Pass")
sns.scatterplot(x = fail_student["StudyHours"],
                y =fail_student["PreviousScore"] , 
                color = "red" ,
                label = "Fail")
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.title("Study Hours v/s Previous Score")
plt.grid(True)
plt.legend()
plt.show()
print("*"*10,"Step 7 Completed","*"*10)

#Boxplot
plt.figure(figsize=(8,5))
sns.boxplot(x="Attendance" , data = df)
plt.title("Boxplot for Attendance")
plt.show()
print("*"*10,"Step 8 Completed","*"*10)

#relation between Assignment completed and Final Result
plt.figure(figsize=(9 , 2))
sns.boxplot(
    x="FinalResult",
    y="AssignmentsCompleted",
    hue = "FinalResult" ,
    palette={
      1 : "green" ,
      0 : "red"
    },
    data=df
)
plt.grid(True)
plt.show()
print("*"*10,"Step 9 Completed","*"*10)

#plot Sleep Hours vs Final Result
plt.figure(figsize=(9 , 5))
sns.boxplot(x="FinalResult",
            y="SleepHours",
            data = df,
            hue = "FinalResult",
            palette={
              1 : "Green" ,
              0 : "Red"
            }
            )
plt.xlabel("Sleep Hours")
plt.ylabel("Final Result")
plt.title("Sleep Hours v/s Final Result")
plt.grid(True)
plt.legend()
plt.show()
# print("*"*10,"Step 10 Completed","*"*10)



