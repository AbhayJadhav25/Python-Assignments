import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score , confusion_matrix , classification_report
from sklearn.preprocessing import StandardScaler
import joblib

def header(step , title):
    print("="*70)
    print(f"Step {step}  :  {title}".center(60))
    print("="*70)
def loadedPreserveModel(filename):
    load = joblib.load(filename)

    print("\nModel Successfully loaded")
    return load

def PreservedModel(model , filename):
    joblib.dump(model , filename)
    print(f"Model preserved Successfully with name : {filename}\n")

def testModel(x_test , y_test , filename):
    header(4 , "test the model")

    loaded_model = loadedPreserveModel(filename)

    y_pred = loaded_model.predict(x_test)

    accuracy = accuracy_score(y_test , y_pred)

    print("Total Accuracy = ",accuracy*100)



def trainWinePredictorModel(data):
    header(3 , "Train the model")
    X = data.drop('Class' , axis  = 1)
    Y = data['Class']

    x_train , x_test , y_train , y_test = train_test_split(
        X ,
        Y , 
        test_size=0.1 ,
        shuffle=True ,
        random_state=42
    )

    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)

    model = KNeighborsClassifier(n_neighbors=15)
    model = model.fit(x_train_scaled , y_train)
    print("Training Complete")

    PreservedModel(model , "winepredictor.pkl")

    testModel(x_test_scaled , y_test , "winepredictor.pkl")

def cleanDataset(data):
    header(2 , "Clean the Dataset by removing empty rows")

    data.dropna(inplace = True)
    print("\nTotal Rows :  ",data.shape[0])
    print("Total Columns :  ",data.shape[1])

    return data

def  showData(data ,message):
    header(" " ,message )

    print("\nFirst 5 rows of Datset")
    print(data.head())

    print("\nShape of Dataset")
    print(data.shape)

    print("\nColumn Name : ")
    print(data.columns.tolist())

    print("\nMissing Values")
    print(data.isnull().sum())

    print("\nData Describe")
    print(data.describe())


def WineClassifier(Dataset):
    header(1,"Load the Dataset")
    data = pd.read_csv(Dataset)

    showData(data , "Initial Dataset")

    data = cleanDataset(data)

    trainWinePredictorModel(data)
def main():
    WineClassifier("WinePredictor.csv")
if __name__ == "__main__":
    main()