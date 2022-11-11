#!/usr/bin/env python3
# Say you have an encrypted PDF that you have forgotten the password to,
# but you remember it was a single English word. Trying to guess your forgot-
# ten password is quite a boring task. Instead you can write a program that
# will decrypt the PDF by trying every possible English word until it finds one
# that works. This is called a brute-force password attack. Download the text file
# dictionary.txt from https://nostarch.com/automatestuff2/. This dictionary file con-
# tains over 44,000 English words with one word per line.
# Using the file-reading skills you learned in Chapter 9, create a list of
# word strings by reading this file. Then loop over each word in this list, pass-
# ing it to the decrypt() method. If this method returns the integer 0, the pass-
# word was wrong and your program should continue to the next password.
# If decrypt() returns 1, then your program should break out of the loop and
# print the hacked password. You should try both the uppercase and lower-
# case form of each word. (On my laptop, going through all 88,000 uppercase
# and lowercase words from the dictionary file takes a couple of minutes. This
# is why you shouldn’t use a simple English word for your passwords.)
import PyPDF2


def password_breaker(reader: PyPDF2.PdfFileReader, string: str):
    reader.decrypt(string.strip())
    try:
        pdfReader.getPage(0)
    except:
        return
    else:
        return string.strip()


with open('dictionary.txt') as file:
    passwords = file.readlines()
pdfFilePath = 'allminutes_encrypted.pdf'
pdfFile = open(pdfFilePath, 'rb')

for password in passwords:
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    result = password_breaker(pdfReader, password.lower())
    if result:
        print(f'Password is {result.lower()}')
        break
    result = password_breaker(pdfReader, password.upper())
    if result:
        print(f'Password is {result.upper()}')
        break
else:
    print('Password not found')
pdfFile.close()
