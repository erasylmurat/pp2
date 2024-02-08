def my_function():
  print("Hello from a function")

my_function()
#--------------------------------------------------------------------------------------
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
#--------------------------------------------------------------------------------------
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
#--------------------------------------------------------------------------------------
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
#--------------------------------------------------------------------------------------
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
#--------------------------------------------------------------------------------------
def my_functions(food):
  for x in food:
    print(x)
fruits=["apple","banana","cherry"]
my_functions(fruits)
#--------------------------------------------------------------------------------------
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
#--------------------------------------------------------------------------------------
x = lambda a : a + 10
print(x(5))
#--------------------------------------------------------------------------------------
x = lambda a, b : a * b
print(x(5, 6))
#--------------------------------------------------------------------------------------
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
#--------------------------------------------------------------------------------------
def myfunc(n):
  return lambda a : a * n
#--------------------------------------------------------------------------------------
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
#--------------------------------------------------------------------------------------
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))
#--------------------------------------------------------------------------------------
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) 
print(mytripler(11))
#--------------------------------------------------------------------------------------
cars = ["Ford", "Volvo", "BMW"]
#--------------------------------------------------------------------------------------
x = len(cars)
#--------------------------------------------------------------------------------------
for x in cars:
  print(x)
#--------------------------------------------------------------------------------------
cars.append("Honda")
#--------------------------------------------------------------------------------------
cars.pop(1)
#--------------------------------------------------------------------------------------
cars.remove("Volvo")
#--------------------------------------------------------------------------------------
class MyClass:
  x = 5
#--------------------------------------------------------------------------------------
p1 = MyClass()
print(p1.x)
#--------------------------------------------------------------------------------------
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
#--------------------------------------------------------------------------------------
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)
#--------------------------------------------------------------------------------------
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
#--------------------------------------------------------------------------------------
class Person:
  pass
#--------------------------------------------------------------------------------------
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
#--------------------------------------------------------------------------------------
class Student(Person):
  pass
#--------------------------------------------------------------------------------------  