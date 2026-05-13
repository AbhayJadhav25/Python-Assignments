import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.DataFrame({
    'study_hours' : [1,2,3,4,5],
    'sleep_hours' : [7,6,7,6,8],
    'Marks' : [50,55,60,65,70]
})
X = data.drop('Marks',axis =1 )
Y = data['Marks']
model = LinearRegression()
model.fit(X,Y)

print(f"Coefficient of Study_hours =  {model.coef_[0]:.2f}")
print(f"Coefficient of Sleep Hours = {model.coef_[1]}")
print(f"Intercept  =  {model.intercept_:.2f}")