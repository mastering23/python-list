# list
print('---------Case 1----------')
numbers = [1,2,3]

# firstNum = numbers[0]
# SecondNum  = numbers[1]
# thirdNum = numbers[2]

firtNum , *others = numbers

print(firtNum,others)

print('\n---------Case 2----------')

numbers = [1,2,3,4,5,6,7,8,9]
firtNum,secondNum, *others, beforeLastNum ,lastNum = numbers

print(firtNum,secondNum,others,beforeLastNum,lastNum)
