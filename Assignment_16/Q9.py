import itertools
def First_10_Even():
  cnt = 0
  # for i in itertools.count(1):
  #   if(i % 2 == 0):
  #     print(i,end="  ")
  #     cnt+=1
  #     if cnt== 10:
          # break;
  while(cnt<10):
    i = 1
    while(cnt < 10):
      if(i % 2 == 0):
        print(i , end = " ")
        i = i+ 2
        cnt+=1
      else:
        i+=1

def main():
  First_10_Even()
  
if __name__ == "__main__":
  main()