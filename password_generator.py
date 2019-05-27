import string
import random

characters = string.ascii_letters + string.digits + string.punctuation

if __name__ == '__main__':
    print('Welcome to PyPassword generator!')
    length = int(input('Enter the length of the password you want to generate: '))

    password = ''
    while length > 0:
        password += random.choice(characters)
        length -= 1

    #print('Password:', password)

    if len(password) <= 5:
        print('Security level: low')
    elif len(password) <= 8:
        print('Security level: medium')
    elif len(password) <= 12:
        print('Security level: high')
    else:
        print('Security level: excellent')
