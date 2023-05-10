# Program to tell user if the number is prime or not a prime number
num = int(input('Enter any number: '))
counter = 2
isPrime = True
while counter < num:
    if num % counter == 0:
        isPrime = False
        break
    counter = counter + 1

if isPrime:
    print('This is a prime number!')
else:
    print('This is not a prime number!')