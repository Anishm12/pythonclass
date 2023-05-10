fruit1 = input('Enter a fruit:')
fruit2 = input('Enter another fruit:')
fruit3 = input('Enter another fruit:')
fruits = [fruit1, fruit2, fruit3]
toPrint = ', '.join(fruits)
print(toPrint)
def printList(toPrint):
    toPrint = ", ".join(fruits)
    printList(fruits)