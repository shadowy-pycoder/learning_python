#my first python programm guessnumber.py v0.0.1
import random
import sys
import this

attempt = input("Insert Number of attempts: ")
if not attempt.isdigit():
    sys.exit()
else:
    attempt=int(attempt)

min_value = input("Insert min_value: ")
if not min_value.isdigit():
    sys.exit()
else:
    min_value = int(min_value)

max_value = input("Insert max_value: ")
if not max_value.isdigit():
    sys.exit()
else:
    max_value = int(max_value)

if min_value >= max_value:
    print("Invalid values, min >= max")
    sys.exit()

secret = random.randint(min_value, max_value)
#print(secret)
while True:
    if attempt > 0:
       answer = (input(f"Guess a number between {min_value} and {max_value}. You have {attempt} attempts left! \n"))
       if answer == str(secret):
            print("That is the correct answer.")
            print("Winner!")
            break
       else:
            attempt = attempt - 1
            if attempt == 0:
                print("That is not the correct answer. Good luck next time!")
                print("Loser!")
            else:
                print("That is not the correct answer. Please try again!\n")
    else:
        break

