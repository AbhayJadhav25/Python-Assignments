#Difference between bytes sand bytesarray

b = bytes([65,66,67])
# b[0] = 72 #TypeError: 'bytes' object does not support item assignment
print(b)

ba = bytearray([65,66,67])
ba[0] = 72
print(ba)