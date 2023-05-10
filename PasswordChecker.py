# Program to check password and make sure it is 8 or more characters long
username = input('Enter your name: ')
password = input(f'Hello {username}, Please enter your password:')
passwordlength = len(password)
while passwordlength < 8:
    print('Password must be more than 8 characters long')
    password = input('Enter your password:')
    passwordlength = len(password)
hiddenpassword = '*' * len(password)
print(f'Hello {username}, your password is {hiddenpassword}')