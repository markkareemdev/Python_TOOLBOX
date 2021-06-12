
#  empty line spaces before variable declaration really matters in python
#  in python there is no variable declaration like in js.. where yo have let,var and const type of variables respectively


# Data types in python
# 1.
# number data types
# using the typeof all variables must be declared except that of a complex number 
# the coefficient oof the complex variable must be used.

# a = 5
# b = 6.0
# m = 1-1j

# print (a, "is type of ", type(a))
# print (b, "is type of ", type(b))
# print(m,isinstance(1-1j, complex))

#2.
# List data types
# list = [1,2,3,4,5]
# print(list[2])
# using the slicing operator
# print(list[0:4]) 
# changing list item
# list[4] = 6;
# print(list)

# 3
# Tuple data types
# an ordered sequence of items just as a list
# unlike list tuples are immutable once created.
# it values can be extracted using the slicing operator, []
# it is defined with parenthesis ()
# t = (5, "program", 1+4j)
# print(t[1])


#4
#python strings
# a slicing operator can be used here to
# space is also countd as a string here
# strings are also immutable

# s = "This is a string."
# p = ''' A multiLine
#         string'''
# print(s)
# print(p)

# print(s[4:18])


#Python set
# set an unordered collection of unique items
# defined by values seperated by comma inside curly braces
# as an unordered collection of items,
#  indexing or the slicing opertor does not work
# for an the same item, it returns only just one  because the data type is unordred

# a = {5,4,5,6,6,6,7,8} 
# print(a," is a type of " , type(a))
# b = {1,2,3,4,5}
# print(b)

#6
# Python Dictionary
# an unordered collection of key value pairs
# python dictionary is just python set with key value.
# This makes indexing or the slicing operators to work 
# fine with the key value pairs.

# d = {1:'value', 'key':2}
# d[1] = "mark"
# print(d[1], d["key"], type(d))

# Conversion between data types
# coversion functions  int(), float(), str()
# a = int(10.236)
# b = int(-80.268)
# c = int('2')
# d = float('2.5')
# e = str(100)
# favList = [1,2,3,4]
# favWord = ('hello world')
# f = set(favList)
# g = tuple(favList)
# h = list(favWord)

# print(a, b, c, d, e, f, g, h, )
