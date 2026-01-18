def NumberTable(No):
  for i in range(1 , 10+1):
    print(No*i)
    
def main():
  No = int(input("Enter Any Number : "))
  NumberTable(No)

if __name__ == "__main__" :
  main()