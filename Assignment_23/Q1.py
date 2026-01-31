class BookStore :
  NoOfBooks = 0

  def __init__(self):
    name = input("Enter Title of Book : ")
    author = input("Name of Author : ")
    self.Name = name
    self.Author = author
    BookStore.NoOfBooks+=1

  def Display(self):
    print(f"{self.Name} by {self.Author} . No. of books : {BookStore.NoOfBooks}")

def main():
  Obj1 = BookStore()
  Obj1.Display()

  Obj2 = BookStore()
  Obj2.Display()

if __name__ == "__main__":
  main()