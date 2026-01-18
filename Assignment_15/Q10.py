cnt = 0
def EvenCount(No) : 
  global cnt
  if(No%2==0):
    cnt+=1

Even_Count = lambda lst : list(filter(EvenCount , lst))

def main():
    global cnt
    n = int(input("Enter bumber of Elements : "))
    print("Enter Elemnts in List ")
    lst = list()
    for i in range(n):
        Elements = int(input())
        lst.append(Elements)
    Even_Count(lst)
    print("Total Even Number = ",cnt)

 
  
 
if __name__ == "__main__":
  main()