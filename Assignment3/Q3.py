def fun():
  x =10
  print(x)  #10

fun()
print(x) #NameError: name 'x' is not defined. 

#Reason --> in our code we declare variable x inside the function , so it becomes local variable it does'nt have scope outside the function. so the line 6 will generate the error because we not declare the gloabal variable with name x.