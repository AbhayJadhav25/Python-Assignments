from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score , confusion_matrix , classification_report
from sklearn.preprocessing import LabelEncoder
import pandas as pd


def ChcekAccuracy(X , Y):
    x_train , x_test , y_train , y_test = train_test_split(
    X , Y ,
    test_size=0.33 ,
    random_state=42
    )

    k = 6
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(x_train , y_train)
    y_pred = model.predict(x_test)

    Accuracy = accuracy_score(y_test , y_pred)

    for y , yp in zip(y_test , y_pred):
        print(y,"\t",yp)

    print(f"Accuracy of model when k = {k} : {Accuracy*100:.2f}")

    '''
    When K = 3 ,5 ,9 , 6,  7 Accuracy = 73.33% but when we change test_size Accuracy is 100%. 
    '''
def header(step , str):
    border = "="*70
    print(border)
    print(f"{step} : {str}".center(70))
    print(border)
'''
Step 1 : Load and Get the Data
'''
header(1 , "Load and Get the Dataset")

#remove index column 
data = pd.read_csv("PlayPredictor.csv") #while reading pandas ignoring the index column

data.drop(columns = ['Unnamed: 0'] , inplace = True)
print("Data Loaded Successfully")

print("Initial 5 rows of data set")
print(data.head())

'''
step 2 : clean , prepare , and manipulate Data and Analyze it.
'''
header(2 , "clean , prepare , and manipulate Data and Analyze it")

print("Shape of Data")
print(data.shape , "\n")

print("Columns Names")
print(data.columns.to_list(),"\n")

print("Missing Values")
print(data.isnull().sum(), "\n")

print("Data Describe")
print(data.describe())


'''
step 3 : Label Encoding
'''
le = LabelEncoder()
weather_encoder = LabelEncoder()
temp_encoder = LabelEncoder()

data['Whether'] = weather_encoder.fit_transform(data['Whether'])
data['Temperature'] = temp_encoder.fit_transform(data['Temperature'])
data['Play'] =le.fit_transform(data['Play'])

print("==========Data After Label Encoding===========")
print(data.head())


'''
step 4 : Split the Features and Target Value
'''
X = data.drop('Play' , axis = 1)
Y = data['Play']

'''
step 5 : Train the Dataset
'''
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X , Y)

print("Training Complete")

'''
step 6 : Provide new data and test the model
'''
new_data = pd.DataFrame({
    'Whether' : ['Overcast'] ,
    'Temperature' : ['Hot']
})

new_data['Whether'] = weather_encoder.transform(new_data['Whether'])
new_data['Temperature'] = temp_encoder.transform(new_data['Temperature'])

prediction = model.predict(new_data)

if prediction[0] == 1:
    print("Predict : Yes")
else:
    print("Predict : No")

ChcekAccuracy(X , Y)