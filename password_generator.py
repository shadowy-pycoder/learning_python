from random import choice
import sys

def pass_gen_usage():
    print('Usage app.py <size_password> <weak/medium/strong>')


if len(sys.argv) < 3:
    pass_gen_usage()
    sys.exit (1)

try:
    size_password = abs(int(sys.argv[1]))
except ValueError:
    pass_gen_usage()
    sys.exit (1)

type_password = sys.argv[2]

a = {
    '1': '!@#$%^&*()-+?_=,<>/:;.',
    '2': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
    '3': '1234567890',
}

password = ''
a_temp = ''

#size_password = int(input("Size of password: "))


while True:
    #type_password = input("Weak, Medium or Strong password? ").lower()
    if type_password == "weak":
        while size_password:
            a_temp = choice(a['2'])
            password += choice(a_temp)
            size_password -= 1
        print(password)
        break
    elif type_password == "medium":
        while size_password:
            a_temp = choice((a['2'], a['3']))
            password += choice(a_temp)
            size_password -= 1
        print(password)
        break
    elif type_password == "strong":
        while size_password:
            a_temp = choice((a['1'], a['2'], a['3']))
            password += choice(a_temp)
            size_password -= 1
        print(password)
        break
    else:
        pass_gen_usage()
        sys.exit (1)

