a =10
b= 10 
print(id(a)) #140720362386840
print(id(b)) #140720362386840

#id of a and b are same.

a =[10]
b = [10]
print(id(a)) #2324895021056
print(id(b)) #2324894904256

#id of a and b are same in these case because a and b refers to the different list objects therefore id(a)!=id(b)