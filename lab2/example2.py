print(10 > 9)
print(10 == 9)
print(10 < 9)
#-------------------------------------------------------------------------------
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#-------------------------------------------------------------------------------
print(bool("Hello"))
print(bool(15))
#-------------------------------------------------------------------------------
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
#-------------------------------------------------------------------------------
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
#-------------------------------------------------------------------------------
bool(False) # all return false
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
#-------------------------------------------------------------------------------
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))
#-------------------------------------------------------------------------------
def myFunction() :
  return True
print(myFunction())
#-------------------------------------------------------------------------------
def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")
#-------------------------------------------------------------------------------
x = 200
print(isinstance(x, int))
#-------------------------------------------------------------------------------
print(10 + 5)
#-------------------------------------------------------------------------------
print((6 + 3) - (6 + 3))
#-------------------------------------------------------------------------------
print(100 + 5 * 3)
#-------------------------------------------------------------------------------
print(5 + 4 - 7 + 3)
#-------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
print(thislist)
#-------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#-------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#-------------------------------------------------------------------------------
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
#-------------------------------------------------------------------------------
list1 = ["abc", 34, True, 40, "male"]
#-------------------------------------------------------------------------------
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#-------------------------------------------------------------------------------
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
#-------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#-------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#-------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#-------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#-------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#-------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#-------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
#-------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#-------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#-------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
#-------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
#-------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#-------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#-------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#-------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#-------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
#-------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#-------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#-------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#-------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#-------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
del thislist
#-------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#-------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#-------------------------------------------------------------------------------
  thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#-------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
#-------------------------------------------------------------------------------
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
#-------------------------------------------------------------------------------
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
#-------------------------------------------------------------------------------
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
#-------------------------------------------------------------------------------
newlist = [x for x in fruits if x != "apple"]
#-------------------------------------------------------------------------------
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#-------------------------------------------------------------------------------
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#-------------------------------------------------------------------------------
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#-------------------------------------------------------------------------------
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
#-------------------------------------------------------------------------------
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
#-------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#-------------------------------------------------------------------------------
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#-------------------------------------------------------------------------------
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
#-------------------------------------------------------------------------------
list3 = list1 + list2
print(list3)
#-------------------------------------------------------------------------------
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
#-------------------------------------------------------------------------------
for x in list2:
  list1.append(x)
print(list1)
#-------------------------------------------------------------------------------
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#-------------------------------------------------------------------------------
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#-------------------------------------------------------------------------------
thistuple = ("apple",)
print(type(thistuple)) #this is tuple
#-------------------------------------------------------------------------------
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#-------------------------------------------------------------------------------
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#-------------------------------------------------------------------------------
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#-------------------------------------------------------------------------------
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#-------------------------------------------------------------------------------
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
#-------------------------------------------------------------------------------
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
#-------------------------------------------------------------------------------
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#-------------------------------------------------------------------------------
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
#-------------------------------------------------------------------------------
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
#-------------------------------------------------------------------------------
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#-------------------------------------------------------------------------------
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
#-------------------------------------------------------------------------------
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)
#-------------------------------------------------------------------------------
myset = {"apple", "banana", "cherry"}
print(type(myset))
#-------------------------------------------------------------------------------
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
#-------------------------------------------------------------------------------
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
#-------------------------------------------------------------------------------
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
#-------------------------------------------------------------------------------
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
#-------------------------------------------------------------------------------
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
#-------------------------------------------------------------------------------
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
#-------------------------------------------------------------------------------
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
#-------------------------------------------------------------------------------
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}
z = x.symmetric_difference(y)
print(z)
#-------------------------------------------------------------------------------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#-------------------------------------------------------------------------------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#-------------------------------------------------------------------------------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
#-------------------------------------------------------------------------------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
#-------------------------------------------------------------------------------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

x = thisdict.get("model")
#-------------------------------------------------------------------------------
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change
#-------------------------------------------------------------------------------
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change
#-------------------------------------------------------------------------------
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["color"] = "red"
print(x) #after the change
#-------------------------------------------------------------------------------
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["color"] = "red"
print(x) #after the change
#-------------------------------------------------------------------------------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
#-------------------------------------------------------------------------------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict) 
#-------------------------------------------------------------------------------
for x in thisdict:
  print(x)
#-------------------------------------------------------------------------------
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}  
#-------------------------------------------------------------------------------
a = 33
b = 200
if b > a:
  print("b is greater than a")
#-------------------------------------------------------------------------------
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
#-------------------------------------------------------------------------------
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#-------------------------------------------------------------------------------
a = 2
b = 330
print("A") if a > b else print("B")
#-------------------------------------------------------------------------------
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
#-------------------------------------------------------------------------------
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")  
#-------------------------------------------------------------------------------
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")  
#-------------------------------------------------------------------------------
a = 33
b = 200
if b > a:
  pass 
#-------------------------------------------------------------------------------
i = 1
while i < 6:
  print(i)
  i += 1
#-------------------------------------------------------------------------------
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
#-------------------------------------------------------------------------------
i = 0
while i < 6:
  i += 1 
  if i == 3:
    continue
  print(i)
#-------------------------------------------------------------------------------
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
#-------------------------------------------------------------------------------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#-------------------------------------------------------------------------------
for x in "banana":
  print(x)
#-------------------------------------------------------------------------------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break
#-------------------------------------------------------------------------------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#-------------------------------------------------------------------------------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#-------------------------------------------------------------------------------
for x in range(2, 30, 3):
  print(x)
#-------------------------------------------------------------------------------
for x in range(6):
  print(x)
else:
  print("Finally finished!")
#-------------------------------------------------------------------------------
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
