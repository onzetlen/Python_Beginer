print('\t\t\t\t\t\t\t\t\t\t\bIterators and Generators\b\n\n\tan iterable: is an object, not necessarily a data structure \
that can return an iterator.\n')
print('Example for iter() and next() method:\n\n__iter__() method returns the iterator object itself and is used while using for...in\
    \n__next__() method returns the next value, it als o returns a StopIterattion error once all the objects have been traversed.\n')
stocks = ('AAPL', 'MSFT', 'AMZN')
iterator = iter(stocks)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print('\nThe more elegant and automated way is to use a for loop.\
\nThe for loop actually creates an iterator object and executes the next() method for each loop.\n\nenumerate() function\n')
stocks = ['AAPL', 'GOOG', 'TSLA']
en_object = enumerate(stocks)
print('Returns a special enumerate object, which consist of pairs, containing an element of\n an original iterable along with their index within the iterable:')
print(en_object)
print('\nWe can use list() function to convert the enumerate object into a list of tuples:')
print(list(en_object))
print('\nfor index, value in enumerate(stocks):\n\tprint(index,value)\n')
for index, value in enumerate(stocks):
    print(index, value)
print('\nfor index, value in enumerate(stocks, start=10):\n\tprint(index, value)\n')
for index, value in enumerate(stocks, start=10):
    print(index, value)
print('\n(in line 24)\n\nzip() function')
company_names = ['Apple', 'Microsoft', 'Tesla']
tickers = ['AAPL', 'MSFT', 'TSLA']
z = zip(company_names, tickers)
print('\nReturns a zip object:')
print(type(z))
print(z)
print('\nConverting the object into list:')
z_list = list(z)
print(z_list)
print('\nfor company, ticker in z_list:\n\tprint(f\'{ticker} = {company}\')\n')
for company, ticker in z_list:
    print(f'{ticker} = {company}')
print('\nWe can also use the splat operator(*) to print all the elements of z_list:\n',
      * z_list, '\n\nWe are about to make a Counter iterator:\t\t\t\t\tITERATOR$\n')


class Counter(object):
    def __init__(self, start, end):
        """Initialize the object"""
        self.current = start
        self.end = end

    def __iter__(self):
        """Returns itself as an iterator object"""
        return self

    def __next__(self):
        """Returns the next element in the series"""
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


counter = Counter(1, 5)
for element in counter:
    print(element)

print('\nThe code spreading in the 40-50 lines, go check!\n\nCounter class takes two arguments\
 start and end\n__init__() method - constructor, which initializes the object with the star-end parameter received\
\n__iter__() method - returns the iterator object\tand\n__next__() method - computes the next element within the series and return\n')
print('\n\t\t\t\t\t\t\t\tGENERATORS$\n\nTo create a list of the first 10 even digits, we can use the comprehension:\
\n\tIn[]: [numbers*2 for number in range(10)]\n\tOut[]: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]\n\nto return generator object use parantheses():\
\n\tIn[]: (number*2 for number in range(10))\n\tOut[]: <generator object <genexpr> at 0x0000000CE5E656>\n')
numbers = (number for number in range(32, 43))
for nums in numbers:
    print(nums)
numbers = (number for number in range(10))
print('\nWe can also transfer the generator directly to a list.\n\nnumbers = (number for number in range(10))\
\nprint(list(numbers))\n\tOUT:', list(numbers), '\n\nPassing a generator to the next() function:\n')
numbers = (number for number in range(4))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
# print(next(numbers))
print('\nIf we add one more next() function, it raises an error.\nThe evaluation of the expression is delayed\
 until its value is needed.\nIt is also called\tlazy evaluation.\n\nLazy evaluations used when working with\
 extremely large sequences, without store the entire list in memory.\nGENERATE elements of the sequences on the fly.\n')


def counter(start, end):
    """Generate values from start to end."""
    while start <= end:
        yield start
        start += 1


c = counter(1, 5)
print(type(c))
print(list(c))
print('\nUsing the generator implementation saves memory!\n')
