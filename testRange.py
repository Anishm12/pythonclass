# learn range function
user = int(input("Enter a number"))
print(f"These are all the numbers from 1 to {user}: ")
numList = list(range(1, user+1))
print(numList)
print(f'These are all the even numbers from 0 to {user}: ')
evenNumList = list(range(0, user+1, 2))
for num in evenNumList:
    print(num)
print(f"These are all the odd numbers from 1 to {user}: ")
oddNumList = list(range(1, user+1, 2))
for num in oddNumList:
    print(num)
sum = 0
for num in numList:
    sum = sum + num
print(f'This is all of the numbers from 1 to {user} added up: {sum}')
factorial = 1
for num in numList:
    factorial = factorial * num
print(f'The factorial of {user} is {factorial}')