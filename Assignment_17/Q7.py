def display(num):
  for i in range(num):
    for j in range(num):
      print(j+1,end = " ")
    print()

def main():
  display(5)
if __name__ == "__main__":
  main()