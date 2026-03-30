import pandas as pd 
import matplotlib.pyplot as plt
def studentPerformance(): 
    Border = "="*70

    print(Border)
    print("Step 1 : Load the Dataset")
    print(Border)

    df = pd.read_csv(r"D:\Marvellous\Python-Assignments\Assignment_38\student_performance_ml.csv")

    print("FIrst 5 Records")
    print(df.head())

    print("Last of 5 records")
    print(df.tail())

    print("Shape of Dataset = ",df.shape)
    print("Total Number of Rows = ",df.shape[0])
    print("Total Number of Columns = ",df.shape[1])

    print("Column Names")
    print(list(df.columns))

    print("Data type of Each Column")
    print(df.dtypes)

    print(Border)
    print("Total Number of Student in Dataset")
    print(df.shape[0])

    print("Total number of Passed Student")
    print(sum(df["FinalResult"]==1))

    print("Total number of Failed Student")
    print(sum(df["FinalResult"]==0))
    print(Border)
    
    print("Average Study of Hours = ",sum(df["StudyHours"]) / df.shape[0])

    print("Average of Attendance = ",sum(df["Attendance"]) / df.shape[0])

    print("Maximum previous score = ",max(df["PreviousScore"]))
    print("Minimum Sleephours = ",min(df["SleepHours"]))

    print(Border)

    result_distribution = df["FinalResult"].value_counts()
    print("Result Distribution")
    print(result_distribution)
    pass_stud = (sum(df["FinalResult"]==1)/df.shape[0])*100
    print("Average of pass student = ",pass_stud)

    fail_stud = (sum(df["FinalResult"]==0)/df.shape[0])*100
    print("Average of pass student = ",fail_stud)
    print(Border)

    # plt.figure(figsize = (8,5))
    # plt.hist(df["StudyHours"] , bins = 10,color = "skyblue" , edgecolor = "black")
    # plt.title("Study Hours Histogram")
    # plt.xlabel("Study Hours")
    # plt.ylabel("Frequency")
    # plt.grid(True)
    # plt.show()

    df["StudyHours"].plot(kind='hist',edgecolor = "black")
    plt.title("Histogram of Study Hours")
    plt.xlabel("Hours")
    plt.ylabel("Frequency")
    plt.grid(axis='y' , linestyle = '--' )
    plt.show()

    print(Border)
def main():
    studentPerformance()
if __name__ == "__main__":
    main()