# Welcome

# message = 'Lesson One'

# message = 'Bobby\'s Lesson'
# message = "Bobby's Lesson"
# escapes the single quote with a backslash \ or we add double quote around

# message = """You can write multiple lines
# if you have triple quotes"""

# print(len(message))
# gives us the length of the variable

# print(message[0:5])
# you write the index in between []
# the first index is inclusive but the second is not
# you can leave off either the starting or the beginning of it to go till end - begin

# METHODS - FUNCTIONS

# print(message.lower())
# print(message.upper())
# print(message.count())  # count certain no. of charatcers within the string
# print(message.find())  # returns -1 if it can't find anywhere
# you have to change the variable to a new variable when you use .replace() function
# message = message.replace('Lesson', 'Watch')

# CONCATENATION

# greeting = 'Hello'
# name = 'Michael'

# message = '{}, {}. Welcome!'.format(greeting, name)  # python<3.6
# message = f'{greeting}, {name.upper()}. Welcome!'  # f-string   python>3.6

# print(dir(name))  # shows all the attributes and methods we can use for the variable
# print(help(str))
# print(help(str.lower))                              #gives more information of the method


# print(message)
