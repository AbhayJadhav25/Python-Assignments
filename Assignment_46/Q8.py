import pandas as pd
from Q7 import trainModel

model = trainModel()
new_data = pd.DataFrame({
    'study_hours' : [6]
})
y_pred = model.predict(new_data[['study_hours']])
print("Student Marks when Study Hours : 6 = ",y_pred[0])