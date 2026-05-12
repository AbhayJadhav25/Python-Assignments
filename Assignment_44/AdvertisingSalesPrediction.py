import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

'''
Step 1 : Load the Dataset
'''
data = pd.read_csv('Advertising .csv')
print(data.head())
print("Datset Loaded Successfully")

'''
Step 2 : Clean , Prepare and Manipulate Data
'''
print("Initial 5 rows of Dataset")
print(data.head())

print("Column Names : ")
print(data.columns.tolist())

print("Dataset Shape : " , data.shape)

print("Missing Values : \n")
print(data.isnull().sum())

print("Data Describe")
print(data.describe())

'''
Step 3 : Split Dataset into Train test Datset
'''

X = data.drop('sales' , axis = 1)
Y = data['sales']

x_train , x_test , y_train , y_test = train_test_split(
    X , 
    Y , 
    test_size=0.5,
    random_state=42
)

'''
Step 4 : Train the Data
'''
model = LinearRegression()
model.fit(x_train , y_train)

'''
step 5 : Test the Data
'''
y_pred = model.predict(x_test)

'''
step 6 : Disply Predicted Values and Expected Values
'''
print("Expected Values","\t","Predicted Values")
for y , yp in zip(y_test , y_pred):
    print(f"{y} \t\t\t {yp:.2f}")