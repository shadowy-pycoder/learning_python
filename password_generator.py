from random import choice
import sys


def pass_gen_usage():
    print('Usage app.py <size_password> <weak/medium/strong>')

def pass_gen(pass_size, symbols):
    password = ''
    a_temp = ''
    while pass_size:
       a_temp = choice((symbols))
       password += choice(a_temp)
       pass_size -= 1
    return password

if len(sys.argv) < 3:
    pass_gen_usage()
    sys.exit (1)

try:
    size_password = abs(int(sys.argv[1]))
except ValueError:
    pass_gen_usage()
    sys.exit (1)

type_password = sys.argv[2].lower()

a = {
    '1': '!@#$%^&*()-+?_=,<>/:;.',
    '2': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
    '3': '1234567890',
}

if type_password == "weak":
    print(pass_gen(size_password, (a['2'])))
elif type_password == "medium":
    print(pass_gen(size_password, (a['2'], a['3'])))
elif type_password == "strong":
    print(pass_gen(size_password, (a['1'], a['2'], a['3'])))
else:
    pass_gen_usage()
    sys.exit (1)
