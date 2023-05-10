# python file for strings
name = input("Enter your name: ")
# print(name[0])
# print(name[1])
# print(name[2])
# print(len(name))
counter = 0
while counter < len(name):
    print(name[counter])
    counter = counter + 1

# join function
strList = ["Hello", name]
toPrint = ' '.join(strList)
print(toPrint)