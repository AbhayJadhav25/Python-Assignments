def display(num):
  for i in range(num , 0 , -1):
    for j in range(i , 0 ,-1):
      print("*",end = " ")
    print()

def main():
  display(5)
if __name__ == "__main__":
  main()