# python code for reversing a string

name = input('Enter your name: ')
revString = ""
counter = len(name) - 1
while counter >=0:
    revString = revString + name[counter]
    counter = counter - 1

if name == revString:
    print("This word is a palindrome!!!!!!!!!!!!!!!!!!!")
else:
    print(revString)

def reverseString(name):
    revString = ""
    counter = len(name) - 1
    while counter >= 0:
        revString = revString + name[counter]
        counter = counter - 1

        return revString
    





