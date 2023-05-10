from math import *

user = input('Hello user. Which side of a right triangle do you want to calculate: a(leg), b(leg), c(hypotenuse)')
if user == 'a':
    B = int(input('what is the b(leg) value'))
    C = int(input('what is the c(hypotenuse) value'))
    A = sqrt(C * C - B * B)
    print (A)
elif user == 'b':
        A = int(input('what is the a(leg) value'))
        C = int(input('what is the c(hypotenuse) value'))
        B = sqrt(C * C - A * A)
        print(B)
elif user == 'c':
            A = int(input('what is the a(leg) value'))
            B = int(input('what is the b(leg) value'))
            C = sqrt(A * A + B * B)
            print(C)
