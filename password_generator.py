from random import choice
import sys

if len(sys.argv) < 3:
    print('Usage app.py <size_password> <weak/medium/strong>')
    sys.exit ( 1 )

arg1 = sys.argv[1]
arg2 = sys.argv[2]

a = {
    '1': '!@#$%^&*()-+?_=,<>/:;.',
    '2': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
    '3': '1234567890',
}

password = ''
a_temp = ''

#size_password = int(input("Size of password: "))
size_password = int(arg1)


while True:
    #type_password = input("Weak, Medium or Strong password? ").lower()
    #if type_password == "weak":
    if arg2 == 'weak':
        while size_password:
            a_temp = choice(a['2'])
            password += choice(a_temp)
            size_password -= 1
        print(password)
        break
    #elif type_password == "medium":
    elif arg2 == 'medium':
        while size_password:
            a_temp = choice((a['2'], a['3']))
            password += choice(a_temp)
            size_password -= 1
        print(password)
        break
    #elif type_password == "strong":
    elif arg2 == 'strong':
        while size_password:
            a_temp = choice((a['1'], a['2'], a['3']))
            password += choice(a_temp)
            size_password -= 1
        print(password)
        break
    else:
        print("Wrong argument!")
        break
