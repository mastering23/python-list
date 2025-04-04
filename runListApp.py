#List
pets = ["bruno","Lola","bruno","Kiki","foxy","Trex","Mini"]

for pet in pets:
  print(pet)

print("---------------------")
for pet in enumerate(pets): # tuplas
  print(pet)

print("---------------------")
for index, pet in enumerate(pets): # tuplas
  print(index,pet)

print("---------------------")

print(pets.count("bruno"))
if"bruno" in pets:
  print(pets.index("bruno"))

print("------------------------")
pets.insert(1,"Teddy")
pets.append("Rocky")
pets.remove("bruno")
pets.pop(3)
del pets[4]
# pets.clear() #clean the whole list a return empty array
print(pets)
