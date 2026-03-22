# Easy Task
n = int(input("Enter the number : " ))
print("Zero" if n == 0 else ("Even" if n % 2 == 0 else "Odd"))

# Medium tasks
# task 1 -- String reserving
example = input("enter the text : ")
print(example[::-1])


# task 2 -- tub sonlar
n = int(input("enter the endpoint : "))
nums = []
for i in range(2, n + 1):
  check = True
  for j in range(2, int(i ** 0.5) + 1):
    if i % j == 0:
      check = False
      break
  if check :
    nums.append(i)
print(nums)

# task - 3 -- count numbers
nums = [int(i) for i in input("Enter the number's list : ").split()]
res  = {}
for a in nums:
  if a in res:
    res[a] += 1
  else :
    res[a] = 1
print(res)

# HARD task -- library

class Book:
  def def __init__(self, title, author):
    self.title = title
    self.author = author
    self.is_borrowed = False

class Library :
  def __init__(self):
    self.books = []
  
  def add_book(self, book):
    for book in self.books:
      if book.title == title:
        if not book.is_borrowed:
          book.is_borrowed = True
          print("Kitob berildi")
          return 
        else:
          print("Kitob band ")
          return 
    print("Mavjud emas")
  
  def return_book(self, title):
    for book in self.books:
      if book.title == title:
        if book.is_borrowed:
          book.is_borrowed = False
          print("Kitob qaytarildi")
          return 
        else :
          print("Bu kitob hali olinmagan")
          return 
    print("Mavjud emas")

  def search_by_author(self, author):
    res = [book.title for book in self.books if book.author == author]
    return res  
