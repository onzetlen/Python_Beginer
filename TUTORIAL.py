# # Exercise 05

# my_age = 34
# my_height = 97
# my_weight = 180
# my_eyes = 'Blue'
# my_teeth = 'White'
# my_hair = 'Yellow'

# print(f"Let's talk about {my_name}.")
# print(f"He's {my_height} inches tall.")
# print(f"He's {my_weight} pounds heavy.")
# print("Actually that's not too heavy.")
# print(f"He's got {my_eyes} eyes and {my_hair} hair.")
# print(f"His teeth are usually {my_teeth} depending on the coffee.")

# total = my_age + my_height + my_weight
# print(f"If I add {my_age}, {my_height}, {my_weight} I get {total}.")

# # Tried to make a converter, without luck this time.

# def converter(a, b):
#     return (a * 2, 54)
#     return (b % 2, 54)


# az = input()('inches')
# bz = input()('centimeters')

# print(f"If I convert {az} I got {bz}.")

# # EXERCISE 6 # Strings and text

# # Python konws it is a string when ' or " was used.
# # When you add variable, f" string is needed.
# # You can apply format to an already-created string wit .format() syntax

# types_of_people = 10
# x = f"There are {types_of_people} types of people."
# binary = "binary"
# do_not = "don't"
# y = f"Those who know {binary} and those who {do_not}."

# print(x)
# print(y)

# print(f"I said: {x}")
# print(f"I also said '{y}'")

# hilarious = False
# joke_evaluation = "Isn't that joke so funny?! {}"

# print(joke_evaluation.format(hilarious))

# w = "This is the left side of..."
# e = "a string with a right side."

# print(w + e)

# # EXERCISE 8

# formatter = "{} {} {} {}"

# print(formatter.format(1, 2, 3, 4))
# print(formatter.format("one", "two", "three", "four"))
# print(formatter.format(True, False, False, True))
# print(formatter.format(formatter, formatter, formatter, formatter))
# print(formatter.format(
#     "Elkiabaltam",
#     "Magam",
#     "de senki se",
#     "Hallott meg engem"
# ))

# # EXERCISE 9 - 10 # Backlash \

# days = "Mon Tue Wed Thu Fri Sat Sun"
# months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# print("Here are the days: ", days)
# print("Here are the months: ", months)

# print("""
#     If I use more than a regular double quote,
#     my lines will printed out
#     the way I was typing it into the text
#     editor.
#     """)

# # This \ (backlash) character encodes difficult-to-type characters into a string.
# # escape the double-quote inside strings

# tabby_cat = "\tI'm tabbed in."
# persian_cat = "I'm split\non a line."
# backlash_cat = "I'm \\ a \\ cat."

# fat_cat = """
# I'll do a list:
# \t* Cat food
# \t* Fishies
# \t* Catnip\n\t* Grass
# """

# print(tabby_cat)
# print(persian_cat)
# print(backlash_cat)
# print(fat_cat)

# # \\          Backlash(\)
# # \'          Single-quote(')
# # \"          Double-quote(")
# # \a          ASCII bell (BEL)
# # \b          ASCII backspace (BS)
# # \f          ASCII formfeed (FF)
# # \n          ASCI linefeed (LF)
# # \N{name}    Character name d name in the Unicdoe database (Unicode only)
# # \r          Carriage return (CR)
# # \t          Horizontal tab (TAB)
# # \uxxxx      Character with 16-bit hex calue xxxx
# # \Uxxxxxxxx  Character with 32-bit hex calue xxxxxxxx
# # \v          ASCI vertical tab (VT)
# # \ooo        Character with octal value ooo
# # \xhh        Character with hex value hh

# # EXERCISE 11 - 12 # Questions # this exercise doesnt work in Sublime text editor


# print("How old are you?, end=' ')
# age = input()

# print("How tall are you?", end=' ')
# height = input()

# print("How much do you weigh?", end=' ')
# weight = input()

# print(f"So, you are {age} old, {height} tall and {weight} heavy.")

# age = input("How old are you? ")
# height = input("How tall are you? ")
# weight = input("How much do you weigh? ")

# print(f"So, you are {age} old, {height} tall and {weight} heavy.")

# # EXERCISE 18 - 19 - 21 # Functions and Variables

# def print_two(*args):
#     arg1, arg2 = args
#     print(f"arg1: {arg1}, arg2: {arg2}")


# def print_two_again(arg1, arg2):
#     print(f"arg1: {arg1}, arg2: {arg2}")


# def print_one(arg1):
#     print(f"arg1: {arg1}")


# def print_none():
#     print("I got nothin'.")


# print_two("Zed", "Shaw")
# print_two_again("Zed", "Shaw")
# print_one("First!")
# print_none()

# def death_and_alive(death_count, number_alive):
#     print(f"There are {death_count} people died!")
#     print(f"Remaining {number_alive} alive.")
#     print("We are not fast enough to save all those people.")
#     print("Hurry up. \n")


# print("We can just give the function numbers directly:")
# death_and_alive(2500, 75000)

# print("OR, we can use variables from our script:")
# death_count = 2720
# number_alive = 76220

# death_and_alive(death_count, number_alive)

# print("we can even do math inside too:")
# death_and_alive(422 + 1000 + 907 + 120, 11340 + 27000 + 40000)

# print("And we can combine the two, variables and math:")
# death_and_alive(death_count + 9000, number_alive + 90000)

# def add(a, b):
#     print(f"ADDING {a} + {b}")
#     return a + b


# def subtract(a, b):
#     print(f"SUBTRACTING {a} - {b}")
#     return a - b


# def multiply(a, b):
#     print(f"MULTIPLYING {a} * {b}")
#     return a * b


# def divide(a, b):
#     print(f"DIVIDING {a} / {b}")
#     return a / b


# print("Let's do some math with just functions!")

# age = add(30, 8)
# height = subtract(78, 4)
# weight = multiply(90, 2)
# iq = divide(100, 2)

# print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# # EXERCISE 24 - 25 # PRACTICE

# print("Let's practice everything.")
# print('You\'d need to know\'bout escapes with \\ that do:')
# print('\n newlines and \t tabs.')

# poem = """
#  \tThe lovely world
#  with the logic so firmly planted
#  cannot discern \n the needs of love
#  nor comprehend passion from intuition
#  and requres an explanation
#  \n\t\twhere there is none.
#  """

# print("-------------")
# print(poem)
# print("-------------")

# five = 10 - 2 + 3 - 6
# print(f"This should be five: {five}")


# def secret_formula(started):
#     jelly_beans = started * 500
#     jars = jelly_beans / 1000
#     crates = jars / 100
#     return jelly_beans, jars, crates


# start_point = 10000
# beans, jars, crates = secret_formula(start_point)

# print("With a starting pont of: {}".format(start_point))
# print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

# start_point = start_point / 10
# print("We can also do this way:")
# formula = secret_formula(start_point)
# print("We'd have {} beans, {} jars, and {} crates.".format(*formula))

# #

# def break_words(stuff):
#     words = stuff.split(' ')
#     return words


# def sort_words(words):
#     return sorted(words)


# def print_first_word(words):
#     word = words.pop(0)
#     print(word)


# def print_last_word(words):
#     word = words.pop(-1)
#     print(word)


# def sort_sentence(sentence):
#     words = break_words(sentence)
#     return sort_words(words)


# def print_first_and_last(sentence):
#     words = break_words(sentence)
#     print_first_word(words)
#     print_last_word(words)


# def print_first_and_last_sorted(sentence):
#     words = sort_sentence(sentence)
#     print_first_word(words)
#     print_last_word(words)

# # EXERCISE 29 - 30  # What If Else

# people = 20
# cats = 30
# dogs = 15

# if people < cats:
#     print("Too many cats! The world is doomed!")

# if people > cats:
#     print("Not many cats! The world is saved!")

# if people < dogs:
#     print("The world is dry!")

# dogs += 5

# if people >= dogs:
#     print("People are greater than or equal to dogs.")

# if people <= dogs:
#     print("People are less than or equal to dogs.")

# if people == dogs:
#     print("People are dogs.")

# #

# people = 30
# cars = 40
# trucks = 19

# if cars > people:
#     print("We should take the cars.")
# elif cars < people:
#     print("We should not take the cars.")
# else:
#     print("We can't decide.")

# if trucks > cars:
#     print("That's too many trucks.")
# elif trucks < cars:
#     print("Maybe we could take the trucks.")
# else:
#     print("We still can't decide.")

# if people > trucks:
#     print("Alright, let's just take the trucks.")
# else:
#     print("Fine, let's stay home then.")

# # EXERCISE 32 - 33 # Loops and Lists

# the_count = [1, 2, 3, 4, 5]
# fruits = ['apples', 'oranges', 'pears', 'apricots']
# change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# for number in the_count:
#     print(f"This is count {number}")

# for fruit in fruits:
#     print(f"A fruit of type: {fruit}")

# for i in change:
#     print(f"I got {i}")

# elements = []
# # the empty list needed for the .append(i)

# for i in range(0, 6):
#     print(f"Adding {i} to the list.")
#     elements.append(i)

# # print(help(list.append))

# for i in elements:
#     print(f"Element was: {i}")

# # print(help(list))

# #

# i = 0
# numbers = []

# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)
#     i = i + 1
#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")

# print("The numbers: ")

# for num in numbers:
#     print(num)

# # EXERCISE 38

# ten_things = "Apples Oranges Crows Telephone Light Sugar"

# print("Wait there are not 10 things in that list. let's fix that.")

# stuff = ten_things.split(' ')
# more_stuff = ["Day", "Night", "Song",
#               "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# while len(stuff) != 10:
#     next_one = more_stuff.pop()
#     print("Adding: ", next_one)
#     stuff.append(next_one)
#     print(f"There are {len(stuff)} items now.")

# print("There we go: ", stuff)

# print("Let's do some things with stuff.")

# print(stuff[1])
# print(stuff[-1])
# print(stuff.pop())
# print(' '.join(stuff))
# print(' # '.join(stuff[3:5]))

# print(help(stuff.pop))
# print(help(ten_things.split))

# # EXERCISE 39 # Dictionaries

# states = {
#     'Oregon': 'OR',
#     'Florida': 'FL',
#     'California': 'CA',
#     'New York': 'NY',
#     'Michigan': 'MI'
# }

# cities = {
#     'CA': 'San Francisco',
#     'MI': 'Detroit',
#     'FL': 'Jacksonville'
# }

# cities['NY'] = 'New York'
# cities['OR'] = 'Portland'

# print('-' * 10)
# print("NY State has: ", cities['NY'])
# print("OR State has ", cities['OR'])
# print('-' * 10)
# print("Michigan's abbreviation is: ", states['Michigan'])
# print("Florida's abbreviation is: ", states['Florida'])
# print('-' * 10)
# print("Michigan has: ", cities[states['Michigan']])
# print("Florida has:", cities[states['Florida']])
# print('-' * 10)
# for state, abbrev in list(states.items()):
#     print(f"{state} is abbreviated {abbrev}")
# print('-' * 10)
# for abbrev, city in list(cities.items()):
#     print(f"{abbrev} has the city {city}")
# print('-' * 10)
# for state, abbrev in list(states.items()):
#     print(f"{state} state is abbreviated {abbrev}")
#     print(f"and has city {cities[abbrev]}")
# print('-' * 10)

# state = states.get('Texas')

# if not state:
#     print("Sorry, no Texas.")

# city = cities.get('TX', 'Does Not Exist')
# print(f"The city for the state 'TX' is: {city}")

# print(help(cities.items))
# print(help(states.get))
# # all attributes and methodes you can do to the list
# print(dir(states))

# # EXERCISE 40 # Modules, Classes, and Objects
# # Python is called an 'OOP' "object-orientated programming language"

# mystuff.py is saved as another document
import mystuff

mystuff.apple()
print(mystuff.tangerine)


class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES")


thing = MyStuff()
thing.apple()
print(thing.tangerine)


class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["\nTHIS is the song ",
                   "That is unsingable",
                   "Without using the Song Class"])

bulls_on_parade = Song(["some more addition",
                        "Just to make sure we remember",
                        "That we have to use commas in between lines."])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

print(help(Song))
