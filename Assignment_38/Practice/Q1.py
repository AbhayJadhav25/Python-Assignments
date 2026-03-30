import pandas as pd 
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


def main():
    studentPerformance()
if __name__ == "__main__":
    main()