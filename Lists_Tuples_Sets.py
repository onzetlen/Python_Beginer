# courses = ['History', 'Math', 'Physics', 'CompSci']

# print(courses[:1])
# # index value will help you print out the selected index only
# print(courses[-1])
# # we can use negative numbers

# # LIST METHODS

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
popped = courses.pop()
nums = [1, 5, 2, 4, 3]

# courses.append('Art')
# # append to the end of the list
courses.insert(0, 'Art')
# # first argument gives the index - position
# courses.insert(0, courses_2)
# # creates an inner list
# courses.extend(courses_2)
# # adds the values at the end of the list
# courses.remove('Math')
# courses.pop()
# # by default it removes the last value of the list
# courses.reverse()
# # reverse the list, last item becomes the first item
# courses.sort()
# # sort by alphabetical order
# nums.sort()
# # sort by ascending order
# courses.sort(reverse=True)
# nums.sort(reverse=True)

# sorted_courses = sorted(courses)
# # it returns a sorted version of the list which you have to print out
# # separately just like .pop  without altering the original list

# print(popped)
print(courses)
# print(sorted_courses)

# print(min(nums))
# print(sum(nums))

# print(courses.index('CompSci'))
# print(courses.index('Methods'))
# # returns -1 if there is no value found
# print('Methods' in courses)
# # return boolean

# for item in courses:
# # looping through each value will be equal to the next value on the list
#     print(item)
# # prints out in separate lines

# for index, course in enumerate(courses start=1):
#     print(index, course)

# course_str = ', '.joint(courses)
# new_list = course_str.split(', ')

# print(course_str)
# print(new_list)

# #TUPLES

# # Mutable
# list_1 = ['History', 'Math', 'Physics', 'CompSci']
# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1[0] = 'Art'

# print(list_1)
# print(list_2)

# # Immutable
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Art'

# print(tuple_1)
# print(tuple_2)

# # SETS

# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# art_courses = {'History', 'Math', 'Art', 'Design'}

# print(cs_courses)
# # it's order changes each time you run it; sets throw away duplicates

# print(cs_courses.intersection(art_courses))
# print(cs_courses.difference(art_courses))
# print(cs_courses.union(art_courses))

# # Empty Lists
# empty_list = []
# empty_list = list()

# # Empty Tuples
# empty_tuple = ()
# empty_tuple = tuple()

# # Empty Sets
# empty_set = {}
# # this is a dictionary, not an empty set
# empty_set = set()
