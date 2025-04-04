numbers = [8,9,1,2,3,4,5,6,7]

# numbers.sort()
# print(numbers)
#
# numbers.sort(reverse=True)
# print(numbers)
print("\n-----------------------------List\n")
numbers2 = sorted(numbers) # return a new list
print(numbers)
print(numbers2)

users = [

  [4,"tonny10"],
  [1,"mark10"],
  [6,"sally"],
  [9,"rose12"]

]
print("\n-----------------------------Sort\n")
users.sort()
print(users)

users = [

  ["tonny10",4],
  ["mark10",1],
  ["sally",6],
  ["rose12",9]

]
print("\n-----------------------------unSort\n")
users.sort()
print(users)

print("\n-----------------------------Sort by using a function\n")
def sortUser(element):
  return element[1]

users.sort(key=sortUser)
print(users)

print("\n----------------------------- Sort by using lambda or Anonymous Functions\n")
users.sort(key=lambda element:element[1])
print(users)