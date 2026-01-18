def PrintNUmber(No):
  for i in range(1 , No+1):
    print(i,end=" ")
    
def main():
  No = int(input("Enter Any Number : "))
  PrintNUmber(No)
  
if __name__ == "__main__" :
  main()