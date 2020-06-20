# Today I am going to tell you the story of the first co existing cat - human relationship.
# It is rather interesting, this crazy bitch fucked everyones mind off.
# Her name was Maya

print(float(5))
print(type(float(5)))
# type gives the class ?? page 30
print(int(5.9))
print(type(int(5.9)))
# above following practice
print(round(5.85))
print(round(1994.39))
# rounds the number to ndigits after decimal point -> round(number, ndigits)
print(round(95.2))
print(round(5.98765, 2))
print(round(5.98765, 1))
# absolute function, takes one numerical argument and returns abs
print(abs(-5))
print(abs(5))
print(abs(5.0))
# pow(a, b) returns a^b
print(pow(5, 5))
print(pow(2, 4))
print(pow(5, 2))
print(pow(2, 6))
# scientific notation
print(5e-1)
print(5e1)
print(5E2)
# formated string literal
stock_name = "AAPL"
print(f'The stock ticker for Apple Inc is {stock_name}.')
# some others for practice
print("AAPL", "is the stock ticker of Apple Inc.")
stock_name = "MFST"
print(stock_name + " is the stock name of Microsoft Corporation.")
# format function
stock_ticker = 'AAPL'
price = 226.41
print('We are interested in {x} which is currently trading at {y}'.format(
    x=stock_ticker, y=price))
# escape new line \n
print('We are interested in {} which is currently\ntrading at {}'.format(
    stock_ticker, price))
# which is also useful for
print('This kind of stuff\'s That\'s really easy.')
# \t tab escape sequence
print('AAPL.\tNIFTY50.\tDJIA.\tNIKKEI500.')
# a single \ at the end of the line
# indicates that the string is continued
print('AAPL is the ticker for Apple Inc. \
It is a technology company.')
# practicing information
name = ('Mirjam', 'Margitta', 'Rahel', 'Janos', 'Barnabas', 'Gellert', 'Gabor')
age = (30, 29, 28, 26, 0, 20, 16)
home = ("HUN", "HUN", "HUN", "UK", "Heaven", "HUN", "HUN")
# still practicing
something = 'Practice produce the master of its subject.'
print(something[0])
print(something[1])
print(something[0:8])
print(name[0:3])
# string methods - operation on string
sample_string = 'elementary school'
print(sample_string.upper())
print(sample_string.lower())
# this returns a string with whitespace removed from the start and end.
print(' A string with whitespace at both the ends.  '.strip())
# this returns the boolean value True if all characters in a string are letters, False otherwise.
print('Alphabets'.isalpha())
print('Life 42'.isalpha())
# the string under evaluation contains whitespace
print('This string contains only alphabets'.isalpha())
# this method returns the boolean value True if all characters in a string are digits, False otherwise.
print('12345'.isdigit())
print('1 2 3'.isdigit())
# return the boolean value True if the first character of a string
# starts with the character provided as an argument, False otherwise.
print('Coca-ine'.startswith('C'))
# same with the ending this time
print('Coca-ine'.endswith('e'))
# this method returns the lowest index in a string where substring sub is found within the slice [start:end]. Start end arguments are optional.
# returns -1 if sub is not found.
print('Going viral this Saturday.'.find('viral'))
# first occurance at index 9
print('Going viral this Saturday.'.find('a'))
# we don't have it in the string
print('Going viral this Saturday.'.find('going'))
# this method returns a copy of the string with all occurences of old replace by new.
print('00 01 10 11'.replace('0', '1'))
print('00 01 10 11'.replace('1', '0'))
# this method is used to split a string into multiple strings based on the argument.
# python outputs the strings in a single data structure called list.
print('AAPL MSFT GOOG'.split(' '))
# this method returns the index of the first occurrence of the character.
# python will provide an error if the character as an argument is not found within the string.
print('Going viral this Saturday'.index('y'))
print('Going viral this Saturday'.index('y'))
# returns a capitalized version of the string.
print('i can not afford living in Chelsea anymore.'.capitalize())
# this method returns a count of an argument provided by character.
print('Going viral this evening.'.count('i'))
print('Going viral this evening'.count('g'))
print('going viral this evening.'.count('g'))
# debugging type() function
print(type('Going viral this Saturday'))
print(type(2020.04))
print(type(2020))
print(type('0'))
print(type(False))
print(type([1, 2, 3]))
print(type({'key': 'value'}))
print(type((1, 2, 3)))
print(type({1, 2, 3}))
# implicit conversion type
print(8 / 2)
# explicit conversion
print('This is the year ' + str(2020))
print(float(4))
print(float('4.2'))
print(int(4.0))
print(int('4'))
# python does not convert a string literal with a fractional part, and instead, it will throw an error.
# add .1 after 2020 to see
print(int('2020'))
print(str(4.2))
print(int(False))
print(int(True))
# python converts 0 to False and rest all integers to True
print(bool(0))
print(bool(1))
print(bool(2000.2))
# # Chapter 4 Modules, Packages, Libraries

# # we can save this module as arithmetic.py and import for later use.
# def addition(a, b):
#     return a + b

# def multiply(a, b):
#     return a * b

# def division(dividend, divisor):
#     return dividend / divisor

# def factorial(n):
#     i = 0
#     result = 1
#     while(i !=n):
#         i = i + n
#         result = result * i
#     return result
# # import arithmetic
# # so just to try I will save this module separately
# # and it works perfectly
import arithmetic

result = arithmetic.addition(2, 3)
print(result)

print(arithmetic.multiply(3, 5))
print(arithmetic.division(10, 4))
print(arithmetic.factorial(5))
# we can print out the name with an overloading operator
print(arithmetic.__name__)
# # python interpreter interactions
import sys
# returns a string containing the copyright pertaining to the python interpreter
print(sys.copyright)
# returns the name of the encoding used to convert between unicode filenames and byte filenames.
print(sys.getfilesystemencoding())
# returns information regarding the Python interpreter
print(sys.implementation)
# returns a string containing a platform identifier
print(sys.platform)
# returns a string containing the version number of the Python interpreter plus additional information on the compiler.
print(sys.version)
# importing statement
import math
import pandas
# accessing functions within math module
print(math.pi)
print(math.floor(10.8))
print(pandas.DataFrame)
# we can also alias a library name while importing it
import math as m
print(m.pi)
print(m.e)
print(m.gamma)
# other way of thinking to import all definitions in that particular module
from math import *
print(pi)
print(ceil(10.2))
# finding a moudle - sys.path
for path in sys.path:
    print(path)
# DIR() names the module defines
print(dir(arithmetic))
# builtins
import builtins
print(dir(builtins))

# # LISTS # #
stock_list = ['HP', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'AMZN', 'NFLX']
print(stock_list[2])
print(stock_list[1:4])
print(stock_list[-1])
print(stock_list)
stock_list[0] = 'NVDA'
stock_list[-3:] = ['AMD', 'GE', 'BAC']
print(stock_list)
# append method adds a single element to the end of the list
# it does not return the new list, just modifies the original list
stock_list.append('AMZN')
print(stock_list)
stock_list.append(['TSLA', 'GE', 'NFLX'])
print(stock_list)
# extend method adds the element to the end of the list.
stock_list.extend(['FRBS', 'NATGEO'])
print(stock_list)
# append() method is used to add a single element to existing list and takes a single element as an argument, whereas the extend() method is used to add multiple elements to existing list and it takes a list as an argument.
# insert(index, element) inserts an item at a given position
stock_list.insert(2, 'ALMA')
print(stock_list)
# remove() removes the first item whose value is element provided in an argument
stock_list.remove('ALMA')
print(stock_list)
# pop() function removes and returns tmethod check whether the calling set contains all elements of the second set
# true 'this_is_A_set' contains all elements of the 'fin_stocks'
# print(this_is_A_set.issuperset(fin_stocks))
# false otherwise
# print(fin_stocks.issuperset(this_is_A_set))

# # TUPLES # #
# it allows storing values of different types together
# immutable, contain a heterogeneous sequence of elements that are accessed via unpacking or indexing
tup = (1, 2, 3)

# # KEYWORDS & OPERATORS # #dex

# 'and' logical operator, return boolean
print((5 > 3) and (4 > 2))
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!! check why give this value 0.0 instead of Boolean
print(((5 / 2) - 2.5) and (0))
# seems like if and operand detects to nill, it will give output as 0.0, interesting
print((4 - 2) and (2))
# ok so it seems like the 0.0 is the arithmetical answer to the arguments give up, without < > and doesn't return boolean
print((66 > 33) and (50 > 29))
# 'as' keyword is used to create an alias
import calendar as c
print(c.isleap(2020))
# 'assert' keyword is used in debugging -> assertion error
assert name == ('Mirjam', 'Margitta', 'Rahel', 'Janos',
                'Barnabas', 'Gellert', 'Gabor')
# the following line will raise an assertion error
# assert name == 'Mirjam'
# 'break' keyword is used to break for & while loops
for i in range(9):
    if i > 3:
        break
    print(i)
# just a check up how for loop works in normal scenario
for i in range(9):
    print(i)
# 'class' keyword is used to creat class


class stock():
    name = 'AAPL'
    price = 224.61


s1 = stock()
print(s1.name)
print(s1.price)
#'continue' keyword is used to end the current iteration in a for & while loops, and continues to the next iteration
for i in range(9):
    if i == 4:
        continue
    else:
        print(i)
#'def' keyword is used to define a function in Python


def python_function():
    print('You just created your first function.')


python_function()
# # 'del' keyword is used to delete objects, it can also be used to delete variables, lists or elements from data structures ...
# del (name)
# print(name)

# 'if' 'elif' 'else' logical operators
number = 5
if number < 5:
    print('Number is less than 5.')
elif number == 5:
    print('Number is equal to 5.')
else:
    print('Number is greater than 5.')

# 'try''except' blocks
try:
    y > 5
except:
    print('Something went wrong.')
# 'finally'  define a code which will run no matter if the try block raises an error or not.
finally:
    print('The try... except code is finished.')

# 'False' 'True' integer value 0 1
buy_flag = False
print(int(False))
buy_flag = True
print(int(True))

# 'for' to define for loop
for i in range(5):
    print(i)
for i in name:
    print(i)
for k in stock_list:
    print(k)
# looping through dictionaries the for loop will print out the key values
# for j in tickers:
    # print(j)
# other examples using the learned 'break' is a total stop nothing will be executed afterwards
for i in ['fa', 'ba', 'be', 'qi']:
    if 'b' in i:
        break
    print(i)
else:
    print('Done.')
# other examples
for i in ['fa', 'ba', 'be', 'qi']:
    if 'b' in i:
        continue
    print(i)
else:
    print('Done.')
# 'import' keyword is used to import external libraries and modules to the current program
import pandas
import numpy
# 'from' keyword is used to import specific modules from libraries
from pandas import DataFrame
from datetime import time
# 'global' keyword is used to declare global variables from non global source ?
takarodj = 'GOOG'


def pelda():
    global takarodj
    takarodj = 'MSFT'


pelda()
print(takarodj)
# 'in' keyword is used to check if the value is present in the sequence
print('GOOG' in stock_list)
print('AMZN' in stock_list)
print(stock_list)
# 'is' keyword is used to test two variables refers to the same object in python. returns boolean
y = stock_list
print(stock_list is y)
# 'lambda' keyword is used to create a small anonymus function in python
# it can take he last item in the list, if index is given as an argument, it removes the item at the given position in the list and returns it.
list2 = stock_list.pop(8)
print(list2)
print(stock_list)
# index() returns the index of the first item whose value is element provided in an argument, otherwise ERROR
print(list2.index('NFLX'))
print(stock_list.index('GE'))
# count() returns the number of times element appears in the list
print(stock_list.count('GOOG'))
# reverse()
stock_list.reverse()
print(stock_list)

# # DICTIONARIES # # and operations with them {key1 : value1, key2 : value2}

tickers = {}
print(type(tickers))
# creating an empty dictionary using the dict() method
tickers = dict()
print(type(tickers))
# altering dictionaries
tickers = {'symbol': 'AAPL', 'price': 224.95, 'company': 'Apple Inc',
           'founded': 1976, 'products': ['Machintos', 'iPod', 'iPhone', 'iPad']}
print(tickers)
print(tickers['symbol'])
tickers['price'] = 225
print(tickers)
print(tickers['products'])
tickers['founders'] = ['Steve Jobs', 'Steve Wozniak', 'Ronald Wayne']
print(tickers)
# deleting any key-value pair in the dictionary use del() function
del(tickers['founders'])
print(tickers)
# how many key-value pair within the list?
print(len(tickers))
# returning all objects
print(tickers.items())
# returning all keys
print(tickers.keys())
# returning all values
print(tickers.values())
# pop() function within lists, pops the item whose key is given as an argument
print(tickers.pop('symbol'))
print(tickers.pop('products'))
print(tickers)
# copying dictionaries
aapl = tickers.copy()
print(aapl)
# this method empties the calling dictionary
tickers.clear()
print(tickers)
# we can also update the lists with the update() method
ticker1 = {'stock': 'NASDAQ', 'price': '7745'}
ticker2 = {'inverstors': ['Warren Buffet', 'Jimmy Cho']}
tickers.update(ticker1)
tickers.update(ticker2)
print(tickers)

# # SET # # is an unordered and unindexed collection of items
# it is a collection data type which is mutable, iterable, and contains no duplicate values
this_is_A_set = {'GOOG', 'AAPL', 'NFLX', 'GE', 'GOOG'}
print(this_is_A_set)
# slicing operation doesn't work
# once a set is created we cannot change its tiems, but we can add new items to it add()
this_is_A_set.add('AMZN')
print(this_is_A_set)
# to add multiple lines use update()
this_is_A_set.update(['FB', 'TSLA'])
print(this_is_A_set)
print(len(this_is_A_set))
# to remove or delete an item we can use the remove() or discard() methods.
# if the item is not present remove() will throw an ERROR whilst discard() will not.
this_is_A_set.remove('FB')
this_is_A_set.discard('GOOG')
this_is_A_set.discard('TWTR')
print(this_is_A_set)
print(len(this_is_A_set))
# we can also empty the set, just like lists or dictionaries
this_is_A_set.clear()
print(this_is_A_set)
# following the mathematical notion, we can perform set operations such as union, intersection, difference...
tech_stocks = {'AMD', 'GOOG', 'AAPL', 'WDC'}
fin_stocks = {'BAC', 'BMO', 'JPLS'}
# union() method allows performing union between sets
this_is_A_set = tech_stocks.union(fin_stocks)
print(this_is_A_set)
# intersection() method performs the intersection between sets
print(this_is_A_set.intersection(fin_stocks))
# difference() method performs a difference operation, leaving the second set out
print(this_is_A_set.difference(fin_stocks))
# issubset() method check whether all elements of calling set is present within a second set or not. returns boolean
# true as the 'this_is_A_set' contains all elements of 'fin_stocks'
print(fin_stocks.issubset(this_is_A_set))
# false as the 'fin_stocks' does not contains all elements of 'this_is_A_set'
print(this_is_A_set.issubset(fin_stocks))
# isdisjoint() method checks for the intersection between two sets
# true none of the set contains any element of each other
print(fin_stocks.isdisjoint(tech_stocks))
# false 'this_is_A_set' set contains element of the 'fin_stocks'
print(fin_stocks.isdisjoint(this_is_A_set))
# issuperset() multiple arguments but accepts only a single expression
# type( addition = lambda x, y : x + y  )


def addition(x, y): return x + y


print(addition(5, 2))


def multiplication(x, y): return x * y


print(multiplication(5, 2))
# 'None' represent NoneType datatype which is nor 0, False or an empty string!
none = None
print(type(none))
# 'nonlocal' keyword is used to declare a value that is not local
# it used to work with variables inside nested functions, where the variable should not belong to the inner function


def main_function():
    x = 'MSFT'

    def nested_function():
        nonlocal x
        x = 'GOOG'
    nested_function()
    return(x)


main_function()
print(main_function)

# 'not' returns the boolean value of True if the expression is not True, False otherwise.
buy = False
print(not buy)
# 'or' returns True is at least one statement is True, otherwise False.
print((5 > 2 or (4 < 2)))
# 'pass' placeholder for Null function instead of throwing an error


def empty_function():
    pass


empty_function()
# # 'raise' keyword is used to raise an error explicitly in a code. ERROR CODE !!!
# x = 'Python'
# if not type(x) is int:
#     raise TypeError('Only integers allowed!')
# 'return' keyword is used to return value from a function or a method


def addition(a, b):
    return a + b


print(addition(2, 5))
# 'with' keyword is used to wrap the execution of a block with methods defined by a context manager
with open('abc.txt', 'a') as file:
    file.write('')

with open('abc.txt', 'r') as file:
    print(file.readline())

# 'and' logical operator returns True if all statements result in True
print(5 == 5 and 3 < 5)


7
