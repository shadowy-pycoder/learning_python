
message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)

message = "Hello Python Crash Course reader!"
print(message)
message = "One of Python's strengths is its diverse community."
print(message)
message = 'One of Python\'s strengths is its diverse community.'
print(message)
message = "Python is the \"best\" language"
print(message)
message = 'Python is the "best" language'
print(message)

name = input ("What is your name?\n")
print("\n"+name.title()) #using methods to deal with letters
print(name.upper())
print(name.lower())

#Combining or Concatenating Strings
first_name = "ada"
last_name = "lovelace"
#full_name = first_name + " " + last_name
full_name = f"{first_name} {last_name}"
#To insert a variable’s value into a string, place
# the letter f immediately before the opening quotation
# mark ➊. Put braces around the name or names of any
# variable you want to use inside the string. Python
# will replace each variable with its value when the
# string is displayed.
#These strings are called f-strings. The f is for
#format, because Python formats the string by
# replacing the name of any variable in braces with
# its value. The
print(full_name)

first_name = "ada"
last_name = "lovelace"
#full_name = first_name + " " + last_name

#print("Hello, " + full_name.title() + "!")
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

#You can use concatenation to compose a message
#and then store the entire message in a variable:

first_name = "ada"
last_name = "lovelace"
#full_name = first_name + " " + last_name
#message = "Hello, " + full_name.title() + "!"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

#F-strings were first introduced in Python 3.6.
# If you’re using Python 3.5 or earlier, you’ll need
# to use the format() method rather than this f syntax.
# To use format(), list the variables you want to use in the string inside the parentheses following
# format. Each variable is referred to by a set of
# braces; the braces will be filled by the values
# listed in parentheses in the order provided:
#full_name = "{} {}".format(first_name, last_name)

#Adding Whitespace to Strings with Tabs or Newlines
#To add a tab to your text, use the character 
#combination \t
print("Python")
print("\tPython")
#To add a newline in a string, use the character
#combination \n:
print("Languages:\nPython\nC\nJavaScript")
#The string "\n\t" tells Python to move to a new line, 
#and start the next line with a tab.
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#To ensure that no whitespace exists at the right end of a string, 
#use the rstrip() method.
favorite_language = 'python '
favorite_language.rstrip()
#To remove the whitespace from the string permanently,
# you have to store the stripped value back into the 
#variable:
favorite_language = 'python '
addition = "three"
favorite_language = favorite_language.rstrip()
print(f"{favorite_language} {addition}")
#You can also strip whitespace from the left side 
#of a string using the lstrip() method or strip 
#whitespace from both sides at once using strip()
import this
age = 23
#message = "Happy " + str(age) + "rd Birthday!"
message = f"Happy {age}rd Birthday!"

print(message)
#When you use integers within strings like this,
#you need to specify explicitly that you want
#Python to use the integer as a string of characters.
#You can do this by wrapping the variable in the str()
#function, which tells Python to represent non-string
#values as strings:

#tasks
print(5 + 3)
print(11-3)
print(4*2)
print(2**3)
print(16/2)
fav_num = input("What is your number? ")
message = f"My favorite number is {fav_num}"
print(message)

#Underscores in Numbers

#When you’re writing long numbers, you can group
# digits using underscores to make large numbers more
# readable:
universe_age = 14_000_000_000
print(universe_age)

#Multiple Assignment

x, y, z = 0, 0, 0
#You need to separate the variable names with commas,
# and do the same with the values, and Python will
# assign each value to its respectively positioned
# variable. As long as the number of values matches
# the number of variables, Python will match them up
# correctly.

#Constants

#A constant is like a variable whose value stays the
# same throughout the life of a program. Python
# doesn’t have built-in constant types, but Python
# programmers use all capital letters to indicate a
# variable should be treated as a constant and never
# be changed:
MAX_CONNECTIONS = 5000
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
#lists
print(bicycles[0]) #print one element of the list
print(bicycles[0].title()) #use method to format print
print(bicycles[-1]) #use this to access the last item
print(bicycles[-2]) #item before the last and so on

#concatenation to create a message based on a value
#from a list.
message = f"My first bicycle was a {bicycles[0].title()}."

print(message)

#The syntax for modifying an element is similar to
#the syntax for accessing an element in a list.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

#Appending Elements to the End of a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#The append() method at ➊ adds 'ducati' to the end 
#of the list without affecting any of the other
motorcycles.append('ducati')
print(motorcycles)

#The append() method makes it easy to build lists 
#dynamically.
motorcycles = [] #create an empty list

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

#using input to append items interactively. DIY
motorcycles = []

#motorcycles.append(input("The first item to add is "))
#motorcycles.append(input("The second item to add is "))
#motorcycles.append(input("The third item to add is "))

print(motorcycles)

#Inserting Elements into a List
#You can add a new element at any position in your 
#list by using the insert() method.
#This operation shifts every other value in the list
#one position to the right:
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)

#Removing an Item Using the del Statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)
#you can no longer access the value that was
#removed from the list after the del statement
#is used.


#Removing an Item Using the pop() Method
#The pop() method removes the last item in a list,
#but it lets you work with that item after removing it.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

#Popping Items from any Position in a List
#pop(index)
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
#Remember that each time you use pop(), the item you 
#work with is no longer stored in the list.

#Removing an Item by Value
#remove(value)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

#use the remove() method to work with a value
#that’s being removed from a list.

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

#The remove() method deletes only the first
#occurrence of the value you specify.

#Sorting a List Permanently with the sort() Method

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#sort this list in reverse alphabetical order
#by passing the argument reverse=True to the sort()
#method.

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

#Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

#Printing a List in Reverse Order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

#Finding the Length of a List using len() function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
#Looping Through an Entire List

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    print(f"{magician.title()}, that was a great trick!")
print("End of the loop")
#add indent 4 spaces before print to make for loop work
#Python uses indentation to determine when one
#line of code is connected to the line above it.
#In the previous examples, the lines that printed
#messages to individual magicians were part of the
#for loop because they were indented. Python’s use
#of indentation makes code very easy to read.

#Making Numerical Lists
#Using the range() Function
for value in range(1,5):
    print(value)

#Using range() to Make a List of Numbers
#convert the results of range() directly into a list
#using the list() function.
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)
#the range() function starts with the value 2
#and then adds 2 to that value. It adds 2 repeatedly
#until it reaches or passes the end value, 11,


#create almost any set of numbers you want to
#using the range() function.
squares = []
for value in range(1, 11):
 square = value ** value
 squares.append(square)
print(squares)

squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)

#Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"The max value is {max(digits)}")
print(f"The min value is {min(digits)}")
print(f"The sum value is {sum(digits)}")

#List Comprehensions
squares = [value**2 for value in range(1,11)]
print(squares)

#Tasks
numbers = list(range(1,10,2))
for number in numbers:
    print(number)
print(max(numbers))
print(min(numbers))
print(sum(numbers))
cubes = [value**3 for value in range (1,20,2)]
print(cubes)

#Working with Part of a List

#Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #prints items 0,1,2 excludes 3
#If you omit the first index in a slice, Python
#automatically starts your slice at the beginning
#of the list:
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])

#A similar syntax works if you want a slice that
#includes the end of a list.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("slice till the end of a list")
print(players[2:])

#if we want to output the last three players
#on the roster, we can use the slice players[-3:]:
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

#Looping Through a Slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())

#Copying a List
#To copy a list, you can make a slice that includes
#the entire original list by omitting the first index
#and the second index ([:]).
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

#an immutable list is called a tuple.
#Defining a Tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#Looping Through All Values in a Tuple
dimensions = (200, 50)
for dimension in dimensions:
	print(dimension)

#Although you can’t modify a tuple, you can assign
#a new value to a variable that holds a tuple.
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)
import random
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw': #sign == checks equlity
        print(car.upper())
    else:
        print(car.title())
#Testing for equality is case sensitive in Python.
#For example, two values with different capitalization
#are not considered equal
#car.lower() == 'audi' if case doesn't matter

#Checking for Inequality
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#Numerical Comparisons
#my DIY guess a number script
attempt = 3
secret = random.randint(0,10)
print(secret)
while True:
    if attempt > 0:
       answer = input("Guess my number(0-10). You have " + str(attempt) + " attempts left! ")
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
                print("That is not the correct answer. Please try again!")
    else:
        break
#for comparisons use ==, >, <, >=, <=

#Using and to Check Multiple Conditions

#To check whether two conditions are both True
#simultaneously, use the keyword and to combine
#the two conditional tests; if each test passes,
#the overall expression evaluates to True. If either
#test fails or if both tests fail, the expression
#evaluates to False.
#age_0 >= 21 and age_1 >= 21

#Using or to Check Multiple Conditions

#The keyword or allows you to check multiple
#conditions as well, but it passes when either or
#both of the individual tests pass. An or expression
#fails only when both individual tests fail.
#age_0 >= 21 or age_1 >= 21

#Checking Whether a Value Is in a List

#To find out whether a particular value is already
#in a list, use the keyword in.

requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings

#Checking Whether a Value Is Not in a List

#Other times, it’s important to know if a value 
#does not appear in a list. You can use the keyword 
#not in this situation.

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

#DIY script to perform comparisons
cars = []
car_num = 0
while car_num < 4:
    #cars.insert(car_num, input("Add your " + str(car_num) + " car in list "))
    cars.append(input(f"Add your {car_num} car in list "))
   # cars[car_num] = car 
    if cars[car_num] == 'audi':
        car_num = car_num + 1
    else:
        print("Retard")
        car_num = car_num + 1
print (cars)

cars = []
for car in range(0,3):
    cars.append(input(f"Add {car} car: "))
    if cars[car] == 'audi':
        print("Retard")
    else:
        print("Not retard")
print(cars)

#simple if statements

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

#If the conditional test at ➊ passes, the first
#block of indented print statements is executed.
#If the test evaluates to False, the else block at ➋
#is executed. Because age is less than 18 this time,
#the conditional test fails and the code in the else
#block is executed:

#The if-elif-else Chain
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
#The elif line at ➋ is really another if test,
# which runs only if the previous test failed.

#Rather than printing the admission price within
#the if-elif-else block, it would be more concise
#to set just the price inside the if-elif-else chain
#and then have a simple print statement that runs 
#after the chain has been evaluated:

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print(f"Your admission cost is ${price}.")

#Using Multiple elif Blocks
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print(f"Your admission cost is ${price}")

#Omitting the else Block
#Python does not require an else block at the end
# of an if-elif chain. Sometimes an else block is
# useful; sometimes it is clearer to use an additional
# elif statement that catches the specific condition
# of interest:

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print(f"Your admission cost is ${price}")

#The else block is a catchall statement. It matches
# any condition that wasn’t matched by a specific
# if or elif test, and that can sometimes include
# invalid or even malicious data. If you have a
# specific final condition you are testing for,
# consider using a final elif block and omit the else
# block. As a result, you’ll gain extra confidence
# that your code will run only under the correct
# conditions.

#Testing Multiple Conditions

#sometimes it’s important to check all of the
# conditions of interest. In this case, you should
# use a series of simple if statements with no elif
# or else blocks. This technique makes sense when
# more than one condition could be True, and you
# want to act on every condition that is True

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
#Checking for Special Items

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

#But what if the pizzeria runs out of green peppers?
# An if statement inside the for loop can handle this
# situation appropriately:
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

#Checking That a List Is Not Empty

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#Using Multiple Lists

#The following example defines two lists. The first
#is a list of available toppings at the pizzeria,
# and the second is the list of toppings that the
# user has requested. This time, each item in
# requested_toppings is checked against the list of
# available toppings before it’s added to the pizza:

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries',
                      'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")

#tasks
numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print(f"{number}st\n")
    elif number == 2:
        print(f"{number}nd\n")
    elif number == 3:
        print(f"{number}rd\n")
    else:
        print(f"{number}th\n")
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

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

#A dictionary in Python is a collection of key-value
#pairs. Each key is connected to a value, and you
#can use a key to access the value associated with
#that key. A key’s value can be a number, a string,
#a list, or even another dictionary.

#Accessing Values in a Dictionary

#To get the value associated with a key, give the
# name of the dictionary and then place the key
# inside a set of square brackets,

alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

#Adding New Key-Value Pairs

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#Starting with an Empty Dictionary

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

#Modifying Values in a Dictionary

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

#We’ll store a value representing the alien’s
# current speed and then use it to determine how
# far to the right the alien should move:
alien_0 = {'x_position': 0, 'y_position': 25,
'speed': 'medium'}
print(f"Original x-position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its
# current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
# This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the
# increment.
alien_0['x_position'] = ( alien_0['x_position'] +
 x_increment )

print(f"New x-position: {alien_0['x_position']}")

#This technique is pretty cool: by changing one value
# in the alien’s dictionary, you can change the
# overall behavior of the alien. For example, to turn
# this medium-speed alien into a fast alien, you would
# add the line:
alien_0['speed'] = 'fast'

#Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

#A Dictionary of Similar Objects
#You can also use a dictionary to store one kind of
# information about many objects.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python', #use comma at the end to continue
    }
print(f"Sarah's favorite language \
        is {favorite_languages['sarah'].title()}.")

#When you know you’ll need more than one line to
# define a dictionary, press ENTER after the opening
# brace. Then indent the next line one level (four
# spaces), and write the first key-value pair,
# followed by a comma. From this point forward when
# you press ENTER, your text editor should automatically
# indent all subsequent key-value pairs to match the
# first key-value pair.

#This example also shows how you can break up a long
# print statement over several lines. The word print
# is shorter than most dictionary names, so it makes
# sense to include the first part of what you want to
# print right after the opening parenthesis ➊. Choose
# an appropriate point at which to break what’s being
# printed, and add a concatenation operator (+) at
# the end of the first line ➋. Press ENTER and then
# press TAB to align all subsequent lines at one
# indentation level under the print statement. When
# you’ve finished composing your output, you can place
# the closing parenthesis on the last line of the print
# block ➌

#Looping Through a Dictionary

#You can loop through all of a dictionary’s key-value
# pairs, through its keys, or through its values.

#Looping Through All Key-Value Pairs
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
#see everything stored in this user’s dictionary
for key, value in user_0.items():
#method items() returns a list of key-value pairs.
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

#Looping Through All the Keys in a Dictionary

#The keys() method is useful when you don’t need
# to work with all of the values in a dictionary.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in favorite_languages.keys():
    print(name.title())

#Looping through the keys is actually the default
# behavior when looping through a dictionary
#keys() can be omitted, but including makes your
#code clearer

#access the value associated with any key you care
# about inside the loop by using the current key.


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(f" Hi {name.title()}, I see your favorite language is {favorite_languages[name].title()}!")

#You can also use the keys() method to find out if
# a particular person was polled.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
print(favorite_languages.keys())

#The keys() method isn’t just for looping: It actually
# returns a list of all the keys, and the line at ➊
# simply checks if 'erin' is in this list.

#Looping Through a Dictionary’s Keys in Order

#You can use the sorted() function to get a copy of
# the keys in order:

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print(favorite_languages.keys())

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

#Looping Through All Values in a Dictionary

#you can use the values() method to return a list of
# values without any keys.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

#To see each language chosen without repetition,
# we can use a set.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

#When you wrap set() around a list that contains
# duplicate items, Python identifies the unique
# items in the list and builds a set from those items.

#Tasks

rivers_countries = {
    'nyle': 'egypt',
    'volga': 'russia',
    'colorado': 'usa',
    'amazon': 'brazil',
    }

for river, country in rivers_countries.items():
    print(river.title() + " runs through " +
        country.title())
for river in rivers_countries.keys():
    print(f"The name of the river is {river.title()}")
for country in rivers_countries.values():
    print(f"The country is {country.title()}")

#Nesting
#Sometimes you’ll want to store a set of dictionaries
# in a list or a list of items as a value in a
# dictionary.

#A List of Dictionaries

#make a list of aliens in which each alien is a
# dictionary of information about that alien.

#create three dictionaries, each representing
# a different alien.

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

#we pack each of these dictionaries into a list
# called aliens.

aliens = [alien_0, alien_1, alien_2]

#loop through the list and print out each alien:

for alien in aliens:
    print(alien)

#In the following example we use range() to create
# a fleet of 30 aliens:

# Make an empty list for storing aliens.
#an empty list to hold all of the aliens that
# will be created.
aliens = []

# Make 30 green aliens.
#At ➊ range() returns a set of numbers, which just
# tells Python how many times we want the loop
# to repeat.
#Each time the loop runs we create a new alien ➋ and
# then append each new alien to the list aliens ➌
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5,
        'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")


#to change the first three aliens to yellow,
#medium-speed aliens worth 10 points each, we could
# do this:
# Make an empty list for storing aliens.

aliens = []

# Make 30 green aliens.
for alien_number in range (0,30):
    new_alien = {'color': 'green', 'points': 5,
         'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show the first 5 aliens.
for alien in aliens[0:5]:
    print(alien)
print("...")

#A List in a Dictionary

# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

#You can nest a list inside a dictionary any time
# you want more than one value to be associated
# with a single key in a dictionary.

#Inside the dictionary’s for loop, we use another
# for loop to run through the list of languages
# associated with each person:

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
    else:
        print(f"\n{name.title()}'s favorite language is:")
    for language in languages:
        print(f"\t{language.title()}")

#A Dictionary in a Dictionary

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

#we start accessing the inner dictionary. The variable
# user_info, which contains the dictionary of user
# information, has three keys: 'first', 'last', and
# 'location'. We use each key to generate a neatly
# formatted full name and location for each person,
# and then print a summary of what we know about each
# user


#Using get() to Access Values

#you can use the get() method to set a default value
# that will be returned if the requested key doesn’t
# exist.
#The get() method requires a key as a first argument.
# As a second optional argument, you can pass the
# value to be returned if the key doesn’t exist:
alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

#Tasks OMG



cities = {
    'vladimir': {
        'country': 'russia',
        'population': '300000',
        'fact': 'founded in 10th century',
        },
    'london': {
        'country': 'england',
        'population': '10 million',
        'fact': 'the capital of great britain',
        },
    'moscow': {
        'country': 'russ',
        'population': '20 million',
        'fact': 'doesn\'t believe tears'
        },
    }

for city, info in cities.items():
    print(f"Name: {city.title()}")
    country = info['country']
    population = info['population']
    fact = info['fact']
    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population}")
    print(f"\tFact: {fact}")
#How the input() Function Works
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

#The input() function takes one argument: the prompt,
# or instructions, that we want to display to the
# user so they know what to do.

#Writing Clear Prompts

#Each time you use the input() function, you should
# include a clear, easy-to-follow prompt that tells
# the user exactly what kind of information you’re
# looking for.

name = input("Please enter your name: ")
print(f"\nHello, {name.title()}!")

#You can assign your prompt to a variable and pass
# that variable to the input() function. This allows
# you to build your prompt over several lines, then
# write a clean input() statement.

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

#The first line assigns the first part of the message
# to the variable prompt. In the second line, the
# operator += takes the string that was assigned to
# prompt and adds the new string onto the end.

#Using int() to Accept Numerical Input

#The int() function converts a string representation
# of a number to a numerical representation, as shown
# here:

age = input("How old are you? ")
age = int(age)
if age >= 18:
    print(f"Your age is over 18, because it is {age}")
else:
    print(f"Your age({age}) is less than 18")

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")


#The Modulo Operator

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

#The for loop takes a collection of items and
# executes a block of code once for each item in the
# collection. In contrast, the while loop runs as
# long as, or while, a certain condition is true.

#The while Loop in Action

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
#(The += operator is shorthand for current_number
# = current_number + 1.)

#Letting the User Choose When to Quit

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

#Using a Flag

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)


#We set the variable active to True ➊ so the program
# starts in an active state. Doing so makes the while
# statement simpler because no comparison is made in
# the while statement itself; the logic is taken care
# of in other parts of the program. As long as the
# active variable remains True, the loop will continue
# running ➋.
#In the if statement inside the while loop, we check
# the value of message once the user enters their
# input. If the user enters 'quit' ➌, we set active
# to False, and the while loop stops. If the user
# enters anything other than 'quit' ➍, we print their
# input as a message.

#Using break to Exit a Loop

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

#Using continue in a Loop

#Rather than breaking out of a loop entirely without
# executing the rest of its code, you can use the
# continue statement to return to the beginning of
# the loop based on the result of a conditional test.

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

#If the modulo is 0 (which means current_number is
# divisible by 2), the continue statement tells
# Python to ignore the rest of the loop and return
# to the beginning. If the current number is not
# divisible by 2, the rest of the loop is executed
# and Python prints the current number:

#Avoiding Infinite Loops


#Using while loops with lists and dictionaries allows
# you to collect, store, and organize lots of input
# to examine and report on later.

#Moving Items from One List to Another

# Start with users that need to be verified,
#  and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed
# users.
#  Move each verified user into the list of confirmed
# users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#We begin with a list of unconfirmed users at
# ➊ (Alice, Brian, and Candace) and an empty list
# to hold confirmed users. The while loop at ➋ runs
# as long as the list unconfirmed_users is not empty.
# Within this loop, the pop() function at ➌ removes
# unverified users one at a time from the end of
# unconfirmed_users. Here, because Candace is last in
# the unconfirmed_users list, her name will be the
# first to be removed, assigned to current_user, and
# added to the confirmed_users list at ➍

#Removing All Instances of Specific Values from a List

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

#Filling a Dictionary with User Input

#make a polling program in which each pass through
# the loop prompts for the participant’s name and
# response. We’ll store the data we gather in a
# dictionary, because we want to connect each response
# with a particular user:

responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
# Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

# Store the response in the dictionary.
    responses[name] = response

# Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

#Tasks

sandwich_orders = ['pastrami', 'club', 'submarine', 'pastrami', 'reuben', 'cheesesteak', 'pastrami']
finished_sandwiches = []

#print("the deli has run out of pastrami!")
#while 'pastrami' in sandwich_orders:
    #sandwich_orders.remove('pastrami')

while sandwich_orders:
    new_sandwich = sandwich_orders.pop()
    if new_sandwich == 'pastrami':
        print("the deli has run out of pastrami!")
        while 'pastrami' in sandwich_orders:
            sandwich_orders.remove('pastrami')
        continue
    print(f"I made your {new_sandwich}!")
    finished_sandwiches.append(new_sandwich)

for finished_sandwich in finished_sandwiches:
    print(f"{finished_sandwich.title()} has been made!")


#Defining a Function
#Here’s a simple function named greet_user() that
# prints a greeting:
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

#The line at ➊ uses the keyword def to inform Python
# that you’re defining a function.
#The parentheses hold that information. In this case,
# the name of the function is greet_user(), and it
# needs no information to do its job, so its
# parentheses are empty.


#The text at ➋ is a comment called a docstring, which
# describes what the function does. Docstrings are
# enclosed in triple quotes, which Python looks for
# when it generates documentation for the functions
# in your programs.

#To call a function, you write the name of the function, followed by any necessary information in
# parentheses, as shown at ➍.

#Passing Information to a Function

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')

#Entering greet_user('jesse') calls greet_user()
# and gives the function the information it needs to
# execute the print() call.

#Arguments and Parameters

#The variable username in the definition of
# greet_user() is an example of a parameter, a piece
# of information the function needs to do its job.
# The value 'jesse' in greet_user('jesse') is an
# example of an argument. An argument is a piece of
# information that’s passed from a function call to
# a function. When we call the function, we place the
# value we want the function to work with in
# parentheses. In this case the argument 'jesse' was
# passed to the function greet_user(), and the value
# was assigned to the parameter username.

#Passing Arguments

#You can use positional arguments, which need to be
# in the same order the parameters were written;
# keyword arguments, where each argument consists of
# a variable name and a value; and lists and
# dictionaries of values.

#Positional Arguments

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

#When we call describe_pet(), we need to provide
# an animal type and a name, in that order.

#Multiple Function Calls

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

#You can use as many positional arguments as you need
# in your functions.

#Order Matters in Positional Arguments

#Keyword Arguments

#You directly associate the name and the value within
# the argument, so when you pass the argument to the
# function, there’s no confusion

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')

#Default Values

#When writing a function, you can define a default
# value for each parameter. If an argument for a
# parameter is provided in the function call, Python
# uses the argument value. If not, it uses the
# parameter’s default value.

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')

#Note that the order of the parameters in the function
# definition had to be changed. Because the default
# value makes it unnecessary to specify a type of
# animal as an argument, the only argument left in
# the function call is the pet’s name. Python still
# interprets this as a positional argument, so if the
# function is called with just a pet’s name, that
# argument will match up with the first parameter
# listed in the function’s definition. This is the
# reason the first parameter needs to be pet_name.

describe_pet('willie')

#To describe an animal other than a dog, you could use
# a function call like this:
describe_pet(pet_name='harry', animal_type='hamster')
#Because an explicit argument for animal_type is
# provided, Python will ignore the parameter’s default
# value.

#When you use default values, any parameter with a
# default value needs to be listed after all the
# parameters that don’t have default values. This
# allows Python to continue interpreting positional
# arguments correctly.

#Return Values

#The return statement takes a value from inside a
# function and sends it back to the line that called
# the function. Return values allow you to move much
# of your program’s grunt work into functions, which
# can simplify the body of your program.

#Returning a Simple Value

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#When you call a function that returns a value, you
# need to provide a variable that the return value
# can be assigned to. In this case, the returned value
# is assigned to the variable musician at ➍

#Making an Argument Optional

def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

#But middle names aren’t always needed, and this
# function as written would not work if you tried to
# call it with only a first name and a last name.

#To make get_formatted_name() work without a middle
# name, we set the default value of middle_name to an
# empty string and move it to the end of the list of
# parameters:

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

#Python interprets non-empty strings as True, so if
# middle_name evaluates to True if a middle name
# argument is in the function call ➋

#we have to make sure the middle name is the last
# argument passed so Python will match up the
# positional arguments correctly ➍.

#Returning a Dictionary

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

#This function takes in simple textual information and
# puts it into a more meaningful data structure that
# lets you work with the information beyond just
# printing it.

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

#We add a new optional parameter age to the function
# definition and assign the parameter the special
# value None, which is used when a variable has no
# specific value assigned to it.
#You can think of None as a placeholder value. In
# conditional tests, None evaluates to False. If the
# function call includes a value for age, that value
# is stored in the dictionary.
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
#Using a Function with a while Loop

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if f_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

#We add a message that informs the user how to quit,
# and then we break out of the loop if the user enters
# the quit value at either prompt.

#Passing a List

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#We define greet_users() so it expects a list of names,
# which it assigns to the parameter names. The
# function loops through the list it receives and
# prints a greeting to each user. At ➊ we define a
# list of users and then pass the list usernames to
# greet_users() in our function call

#Modifying a List in a Function

# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
#  Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

#We can reorganize this code by writing two functions,
# each of which does one specific job.

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

#print_models(unprinted_designs, completed_models)
#show_completed_models(completed_models)
#print(unprinted_designs)

#At ➊ we define the function print_models() with two
# parameters: a list of designs that need to be
# printed and a list of completed models. Given these
# two lists, the function simulates printing each
# design by emptying the list of unprinted designs
# and filling up the list of completed models. At ➋
# we define the function show_completed_models() with
# one parameter: the list of completed models. Given
# this list, show_completed_models() displays the name
# of each model that was printed.

#Remember that you can always call a function from
# another function, which can be helpful when
# splitting a complex task into a series of steps.

#Preventing a Function from Modifying a List

#you can address this issue by passing the function
# a copy of the list, not the original. Any changes
# the function makes to the list will affect only the
# copy, leaving the original list intact.

#You can send a copy of a list to a function like this:
#function_name(list_name[:])
#The slice notation [:] makes a copy of the list to
# send to the function. If we didn’t want to empty the
# list of unprinted designs in printing_models.py, we
# could call print_models() like this:
#print_models(unprinted_designs[:], completed_models)

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)

#Passing an Arbitrary Number of Arguments

#Sometimes you won’t know ahead of time how many
# arguments a function needs to accept. Fortunately,
# Python allows a function to collect an arbitrary
# number of arguments from the calling statement.

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#The asterisk in the parameter name *toppings tells
# Python to make an empty tuple called toppings and
# pack whatever values it receives into this tuple.

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#This syntax works no matter how many arguments the
# function receives.

#Mixing Positional and Arbitrary Arguments

#If you want a function to accept several different
# kinds of arguments, the parameter that accepts an
# arbitrary number of arguments must be placed last
# in the function definition. Python matches
# positional and keyword arguments first and then
# collects any remaining arguments in the final
# parameter.

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#You’ll often see the generic parameter name *args,
# which collects arbitrary positional arguments
# like this.

#Using Arbitrary Keyword Arguments

#Sometimes you’ll want to accept an arbitrary number
# of arguments, but you won’t know ahead of time what
# kind of information will be passed to the function.
# In this case, you can write functions that accept
# as many key-value pairs as the calling statement
# provides.

#The function build_profile() in the following example
# always takes in a first and last name, but it accepts
# an arbitrary number of keyword arguments as well:

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')
print(user_profile)

#The double asterisks before the parameter **user_info
# cause Python to create an empty dictionary called
# user_info and pack whatever name-value pairs it
# receives into this dictionary. Within the function,
# you can access the key-value pairs in user_info just
# as you would for any dictionary.

#You’ll often see the parameter name **kwargs used to
# collect non-specific keyword arguments.

#Storing Your Functions in Modules

#An import statement tells Python to make the code in
# a module available in the currently running program
# file.

#Importing an Entire Module

#To start importing functions, we first need to create
# a module. A module is a file ending in .py that
# contains the code you want to import into your
# program. Let’s make a module that contains the
# function make_pizza(). To make this module, we’ll
# remove everything from the file pizza.py except the
# function make_pizza():

#file pizza.py in the same directory

#This file imports the module we just created and then makes two calls to make_pizza():
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#When Python reads this file, the line import pizza
# tells Python to open the file pizza.py and copy
# all the functions from it into this program.

#To call a function from an imported module, enter
# the name of the module you imported, pizza, followed
# by the name of the function, make_pizza(), separated
# by a dot ➊. This code produces the same output as
# the original program that didn’t import a module:

#This first approach to importing, in which you simply
# write import followed by the name of the module,
# makes every function from the module available in
# your program. If you use this kind of import
# statement to import an entire module named
# module_name.py, each function in the module is
# available through the following syntax:

#module_name.function_name()

#Importing Specific Functions

#You can also import a specific function from a module.
# Here’s the general syntax for this approach:

#from module_name import function_name

#You can import as many functions as you want from
# a module by separating each function’s name with a
# comma:
#from module_name import function_0, function_1,
# function_2

from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#With this syntax, you don’t need to use the dot
# notation when you call a function.

#Using as to Give a Function an Alias

#If the name of a function you’re importing might
# conflict with an existing name in your program or
# if the function name is long, you can use a short,
# unique alias—an alternate name similar to a nickname
# for the function.

from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

#The general syntax for providing an alias is:
#from module_name import function_name as fn

#Using as to Give a Module an Alias

import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#The general syntax for this approach is:
#import module_name as mn

#Importing All Functions in a Module

#You can tell Python to import every function in a
# module by using the asterisk (*) operator:

from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#If you specify a default value for a parameter, no
# spaces should be used on either side of the equal
# sign:
#def function_name(parameter_0, parameter_1='default value')

#The same convention should be used for keyword
# arguments in function calls:
#function_name(value_0, parameter_1='value')
"""A class that can be used to represent a car."""

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
            Set the odometer reading to the given value.
            Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
            Initialize attributes of the parent class.
            Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
#Creating the Dog Class

class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

#At ➊ we define a class called Dog. By convention,
# capitalized names refer to classes in Python. There
# are no parentheses in the class definition because
# we’re creating this class from scratch. At ➋ we
# write a docstring describing what this class does.
#The __init__() Method
#A function that’s part of a class is a method.
# Everything you learned about functions applies to
# methods as well; the only practical difference for
# now is the way we’ll call methods. The __init__()
# method at ➌ is a special method that Python runs
# automatically whenever we create a new instance
# based on the Dog class. This method has two leading
# underscores and two trailing underscores, a
# convention that helps prevent Python’s default
# method names from conflicting with your method names.
# Make sure to use two underscores on each side of
# __init__(). If you use just one on each side, the
# method won’t be called automatically when you use
# your class, which can result in errors that are
# difficult to identify.
#We define the __init__() method to have three
# parameters: self, name, and age. The self parameter
# is required in the method definition, and it must
# come first before the other parameters. It must be
# included in the definition because when Python calls
# this method later (to create an instance of Dog),
# the method call will automatically pass the self
# argument. Every method call associated with an
# instance automatically passes self, which is a
# reference to the instance itself; it gives the
# individual instance access to the attributes
#and methods in the class. When we make an instance of
# Dog, Python will call the __init__() method from
# the Dog class. We’ll pass Dog() a name and an age
# as arguments; self is passed automatically, so we
# don’t need to pass it. Whenever we want to make an
# instance from the Dog class, we’ll provide values
# for only the last two parameters, name and age.
#The two variables defined at ➍ each have the prefix
# self. Any variable prefixed with self is available
# to every method in the class, and we’ll also be able
# to access these variables through any instance
# created from the class. The line self.name = name
# takes the value associated with the parameter name
# and assigns it to the variable name, which is then
# attached to the instance being created. The same
# process happens with self.age = age. Variables that
# are accessible through instances like this are
# called attributes.
#The Dog class has two other methods defined: sit()
# and roll_over() ➎. Because these methods don’t need
# additional information to run, we just define them
# to have one parameter, self. The instances we create
# later will have access to these methods. In other
# words, they’ll be able to sit and roll over. For
# now, sit() and roll_over() don’t do much. They
# simply print a message saying the dog is sitting or
# rolling over. But the concept can be extended to
# realistic situations: if this class were part of
# an actual computer game, these methods would contain
# code to make an animated dog sit and roll over. If
# this class was written to control a robot, these
# methods would direct movements that cause a robotic
# dog to sit and roll over.

#Making an Instance from a Class

my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

#At ➊ we tell Python to create a dog whose name is
# 'Willie' and whose age is 6. When Python reads this
# line, it calls the __init__() method in Dog with the
# arguments 'Willie' and 6. The __init__() method
# creates an instance representing this particular dog
# and sets the name and age attributes using the
# values we provided. Python then returns an instance
# representing this dog. We assign that instance to
# the variable my_dog. The naming convention is
# helpful here: we can usually assume that a
# capitalized name like Dog refers to a class, and a
# lowercase name like my_dog refers to a single
# instance created from a class.

#Accessing Attributes

#To access the attributes of an instance, you use dot
# notation. At ➋ we access the value of my_dog’s
# attribute name by writing:
#my_dog.name
#Dot notation is used often in Python. This syntax
# demonstrates how Python finds an attribute’s value.
# Here Python looks at the instance my_dog and then
# finds the attribute name associated with my_dog.
# This is the same attribute referred to as self.name
# in the class Dog. At ➌ we use the same approach to
# work with the attribute age.

#Calling Methods

my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()

#To call a method, give the name of the instance
# (in this case, my_dog) and the method you want to
# call, separated by a dot. When Python reads
# my_dog.sit(), it looks for the method sit() in the
# class Dog and runs that code. Python interprets the
# line my_dog.roll_over() in the same way.

#Creating Multiple Instances

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

#Even if we used the same name and age for the second
# dog, Python would still create a separate instance
# from the Dog class. You can make as many instances
# from one class as you need, as long as you give each
# instance a unique variable name or it occupies a
# unique spot in a list or dictionary.

#Tasks

class Restaurant:
    """Modeling a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type attributes""" 
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        """Describing a restaurant"""
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"Cuisine: {self.cuisine_type}")
    def open_restaurant(self):
        """Opening notice"""
        print(f"{self.restaurant_name} is open!")
    
restaurant = Restaurant('Shanghai', 'chinese')
restaurant_en = Restaurant('Hooligans', 'english')

print(f"My restaurant {restaurant.restaurant_name} serves {restaurant.cuisine_type} food!")
restaurant.describe_restaurant()
restaurant.open_restaurant
restaurant_en.describe_restaurant()
restaurant_en.open_restaurant

#Working with Classes and Instances

#You can use classes to represent many real-world
# situations. Once you write a class, you’ll spend
# most of your time working with instances created
# from that class. One of the first tasks you’ll want
# to do is modify the attributes associated with a
# particular instance. You can modify the attributes
# of an instance directly or write methods that update
# attributes in specific ways.

#The Car Class

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

#Setting a Default Value for an Attribute

#When an instance is created, attributes can be
# defined without being passed in as parameters.
# These attributes can be defined in the __init__()
# method, where they are assigned a default value.

class Car:

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#This time when Python calls the __init__() method to
# create a new instance, it stores the make, model,
# and year values as attributes like it did in the
# previous example. Then Python creates a new
# attribute called odometer_reading and sets its
# initial value to 0 ➊. We also have a new method
# called read_odometer() at ➋ that makes it easy to
# read a car’s mileage.

#Modifying Attribute Values

#You can change an attribute’s value in three ways:
# you can change the value directly through an instance,
# set the value through a method, or increment the
# value (add a certain amount to it) through a method.
# Let’s look at each of these approaches.

#Modifying an Attribute’s Value Directly

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#At ➊ we use dot notation to access the car’s
# odometer_reading attribute and set its value directly.
# This line tells Python to take the instance
# my_new_car, find the attribute odometer_reading
# associated with it, and set the value of that
# attribute to 23:

#Modifying an Attribute’s Value Through a Method

class Car:

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name.\
"""
        long_name = f"{self.year} {self.make}\
 {self.model}"
        return long_name.title()

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the\
 odometer back.
           """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def read_odometer(self):
        """Print a statement showing the car's mileage.\
"""
        print(f"This car has {self.odometer_reading}\
 miles on it.")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()
my_new_car.update_odometer(21)

#If the new mileage, mileage, is greater than or equal
# to the existing mileage, self.odometer_reading, you
# can update the odometer reading to the new mileage ➊.
# If the new mileage is less than the existing mileage,
# you’ll get a warning that you can’t roll back an
# odometer ➋

#Incrementing an Attribute’s Value Through a Method

class Car:

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def read_odometer(self):
        """Print a statement showing the car's mileage.\
        """
        print(f"This car has {self.odometer_reading} miles on it.")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

#You can use methods like this to control how users
# of your program update values such as an odometer
# reading, but anyone with access to the program can
# set the odometer reading to any value by accessing
# the attribute directly. Effective security takes
# extreme attention to detail in addition to basic
# checks like those shown here.

#Inheritance

#You don’t always have to start from scratch when
# writing a class. If the class you’re writing is a
# specialized version of another class you wrote, you
# can use inheritance. When one class inherits from
# another, it takes on the attributes and methods of
# the first class. The original class is called the
# parent class, and the new class is the child class.
# The child class can inherit any or all of the
# attributes and methods of its parent class, but
# it’s also free to define new attributes and methods
# of its own.

#The __init__() Method for a Child Class

#When you’re writing a new class based on an existing
# class, you’ll often want to call the __init__()
# method from the parent class. This will initialize
# any attributes that were defined in the parent
# __init__() method and make them available in the
# child class.

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

#At ➊ we start with Car. When you create a child class,
# the parent class must be part of the current file
# and must appear before the child class in the file.
# At ➋ we define the child class, ElectricCar. The
# name of the parent class must be included in
# parentheses in the definition of a child class.
# The __init__() method at ➌ takes in the information
# required to make a Car instance.
#The super() function at ➍ is a special function that
# allows you to call a method from the parent class.
# This line tells Python to call the __init__() method
# from Car, which gives an ElectricCar instance all
# the attributes defined in that method. The name
# super comes from a convention of calling the parent
# class a superclass and the child class a subclass.
#We test whether inheritance is working properly by
# trying to create an electric car with the same kind
# of information we’d provide when making a regular
# car. At ➎ we make an instance of the ElectricCar
# class and assign it to my_tesla. This line calls the
# __init__() method defined in ElectricCar, which in
# turn tells Python to call the __init__() method
# defined in the parent class Car. We provide the
# arguments 'tesla', 'model s', and 2019.

#Defining Attributes and Methods for the Child Class

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
            Initialize attributes of the parent class.
            Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

#At ➊ we add a new attribute self.battery_size and set
# its initial value to, say, 75. This attribute will
# be associated with all instances created from the
# ElectricCar class but won’t be associated with any
# instances of Car. We also add a method called
# describe_battery() that prints information about the
# battery at ➋. When we call this method, we get a
# description that is clearly specific to an electric
# car:

#Overriding Methods from the Parent Class

#Say the class Car had a method called fill_gas_tank().
# This method is meaningless for an all-electric
# vehicle, so you might want to override this method.
# Here’s one way to do that:
#class ElectricCar(Car):
    #--snip--

    #def fill_gas_tank(self):
        #"""Electric cars don't have gas tanks."""
        #print("This car doesn't need a gas tank!")

#Now if someone tries to call fill_gas_tank() with an
# electric car, Python will ignore the method
# fill_gas_tank() in Car and run this code instead.
# When you use inheritance, you can make your child
# classes retain what you need and override anything
# you don’t need from the parent class.

#Instances as Attributes

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

#At ➊ we define a new class called Battery that doesn’t
# inherit from any other class. The __init__() method
# at ➋ has one parameter, battery_size, in addition to
# self. This is an optional parameter that sets the
# battery’s size to 75 if no value is provided. The
# method describe_battery() has been moved to this
# class as well ➌.
#In the ElectricCar class, we now add an attribute
# called self.battery ➍. This line tells Python to
# create a new instance of Battery (with a default
# size of 75, because we’re not specifying a value)
# and assign that instance to the attribute
# self.battery. This will happen every time the
# __init__() method is called; any ElectricCar instance
# will now have a Battery instance created
# automatically.
#We create an electric car and assign it to the
# variable my_tesla. When we want to describe the
# battery, we need to work through the car’s battery
# attribute:
#my_tesla.battery.describe_battery()
#This line tells Python to look at the instance
# my_tesla, find its battery attribute, and call the
# method describe_battery() that’s associated with the
# Battery instance stored in the attribute.

#Let’s add another method to Battery that reports the
# range of the car based on the battery size:

my_tesla.battery.get_range()

#Importing a Single Class

#car.py method is in the same directory

#At ➊ we include a module-level docstring that briefly
# describes the contents of this module. You should
# write a docstring for each module you create.

from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#The import statement at ➊ tells Python to open the car
# module and import the class Car. Now we can
# use the Car class as if it were defined in this file.

#Storing Multiple Classes in a Module

#You can store as many classes as you need in a single
# module, although each class in a module should be
# related somehow.


from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#Importing Multiple Classes from a Module

from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

#Importing an Entire Module

#You can also import an entire module and then access
# the classes you need using dot notation. This
# approach is simple and results in code that is easy
# to read. Because every call that creates an instance
# of a class includes the module name, you won’t have
# naming conflicts with any names used in the current
# file.

import car

my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

#At ➊ we import the entire car module. We then access
# the classes we need through
# the module_name.ClassName syntax.
# At ➋ we again create a Volkswagen Beetle, and at ➌
# we create a Tesla Roadster.

#Importing All Classes from a Module

#from module_name import *

#"""A set of classes that can be used to represent electric cars."""

#from car import Car

#class Battery:
    #--snip--

#class ElectricCar(Car):
    #--snip--

#from car import Car
#from electric_car import ElectricCar

#At ➊ we import Car from its module, and ElectricCar
# from its module. We then create one regular car and
# one electric car.

#Using Aliases

#from electric_car import ElectricCar as EC

#my_tesla = EC('tesla', 'roadster', 2019)

#The Python Standard Library

#One interesting function from the random module is
# randint(). This function takes two integer arguments
# and returns a randomly selected integer between
# (and including) those numbers.
#Here’s how to generate a random number between 1 and
# 6:
#>>> from random import randint
#>>> randint(1, 6)
#3

#Another useful function is choice(). This function
# takes in a list or tuple and returns a randomly
# chosen element:
#>>> from random import choice
#>>> players = ['charles', 'martina', 'michael', 'florence', 'eli']
#>>> first_up = choice(players)
#>>> first_up
#'florence'
from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
