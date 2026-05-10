list = [10,"Anil" , 89.09 , True]
tuple = (10 , "Anil" , 89.09 , True)
print(list)
print(tuple)

#Mutability
# list[1] = "Om"
# print(list)  #List is mutable

# tuple[1] = "Hari"
# print(tuple) #TypeError: 'tuple' object does not support item assignment. Tuple is immutable


#Memory
print(id(list)) #2632001370112
print(id(tuple)) #2090351176144
 #Both holds different memory address , no matter elements are same or not


 #