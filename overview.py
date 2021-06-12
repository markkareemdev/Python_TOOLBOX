
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

# listList = [[31,26],[3,4]]
# listTuple = [(2,6), (4,6)]

# print(a, b, c, d, e, f, g, h, )

#To convert to dictionary each element must be pair
# print(dict(listList))
# print(dict(listTuple))


# Number System in python
# 1. Binary : The prefix is "0b" or "0B"
# 2. octal  : The prefix is "0c" or "0C"
# 3. Hexadecimal  : The prefix is "0x" or "0X"
# print( 0b1101011, 0xFB + 0b10, 0o15) // 107 253 13

#Python decimal
# print( 1.1 + 2.2 == 3.3) 
# print( 1.1 + 2.2) 

# returns false
# why? is that because the computer understands binary(0 and 1) therefore floating numbers are implemented into computer hardware as binary fractions.
# The decimal of 1/3 which is 0.33333333 will result in an infinitely long binary fraction  but our computer can only store a finite number of it.
# This is an error as a result of truncation caused by COMPUTER HARDWARE, as it can only takes a finite number to represent any binary fraction.
# This is hardware limitation and not python.
# The solution is to use a binary module , this gives approximation to the 15th digti.
# without decimal
# print(3.1)
# with decimal
# import decimal
# print(decimal.Decimal(3.1))
# Another decimal module example.
# from decimal import Decimal as D
# print(D("1.1") + D("1.2"))
# print(D("1.1") * D("1.20"))

# why not use decimal all the time since it is far more accurate?
    # The reason is that floating point operations are more faster
# Areas where decimal modules are needed.
    # 1. financial applications
    # 2. when a controlled level precision is required.
    # 3. when we want to specify  a decimal places.


# Python Fractions
    # it runs fractional operation through the fraction module.
# Example 1
# import fractions
# print(fractions.Fraction(2.7))
# print(fractions.Fraction("2.7"))

# Example 2
# from fractions import Fraction as F
# This gives a short equivalent 
# print(F("2.1")) 
# print(F(2.1))
# print(F(1,3))
# print(F(1,3) + F(2,3))
# print(F(1,3) > 0)

# python mathematics
# python uses modules like math and random to carry out basically math operations
# python math module
# import math
# print(math.pi)
# print(math.cos(math.pi))
# print(math.cos(math.pi))
# print(math.exp(10))
# print(math.log10(1000))
# print(math.sinh(1))
# print(math.factorial(6))
# python random module
# import random
# random values between two points
# y = random.randrange(10,20)
# print(y)
# choiced rearrangement on x
# x = ["a", "b", "c", "d"]
# print(random.choice(x))
# randomized x
# random.shuffle(x) 
# Print randomized x
# print(x)
# Print random element
# print(random.random())

# Python variables
# python allows for chain assignment
# n = 300
# k = g = h = 400
# p = l = "i am a string variable"
# print(n,k,g,h)
# print(type(n))
# print(type(p))
# print(type(2+1j))
# print(isinstance(2+1j,complex))

# Python id: this is just to show two variable points to the same object when variable chaining is used
# n = m = 400
# print(n)
# print(id(n))
# print(id(m))

#Python naming
# The first character of a variable cannot be  a digit
# all other combination is allowed.
# Naming Conventions
    # camel Case: olawaleKareemOwolabi
    # pascal case: OlawaleKareemOwolabi
    # snake case: olawale_kareem_owolabi

# Style guide for python code or PEP8,
# suggests standardised naming convention
# snake case for functions and variable names
# pascal case for class

# python reserved keywords

# False, def, if, raise, None, del, import, return, True, elif, in try, and, else, is, while
# as, except, lambda, with, assert, finally, nonlocal, yield, break, for, not, class, from, or,
# continue, global, pass
# note some keywords are in caps while some are in small letters

# Python Operators
# Python operations includes
    # 1. Arithmethic
    # 2. Relational: runs comparison btw two objects and returns bool e.g >,<,=,!=
    # 3. logical: uses logical operators and returns boolean e.g or,and, not.
# Python Operators
    # Unary operator: require a single operand
    # Binary operaors: requires multiple operand.
# python arithmetic operators
    # Addition: +
    # subtraction: -
    # multiplication: *
    # division: /
    # modulus: %
    # Exponential **
    # Floor division //
# python Assignment operators
    # assignment because "=" is involved
    # x = 5
    # x = x + 4 # same as,x += 4
    # x = x - 4 # same as,x -= 4
    # x = x ^ 3 # same as, x ^= 3 
    # x = x * 3 # same as, x *= 3 
    # x = x ** 3 # same as, x ^= 3 
    # x = x / 3 # same as, x /= 3 
    # x = x % 3 # same as, x %= 3 
    # x = x & 3 # same as,x &= 3
    # x = x | 3 # same as,x|=3
    # x = x >> 3 # x >>= 3
    # x = x << 3 # x <<= 3

    # print(x)

# Python Logical operators
    # and: x<5 & x<10
    # or: x<5 or x<10
    # not: not(x<5 & x<10)

# python identity operators
    # is  ,returns a boolean, usage: x is y
    # is not , ,returns a boolean, usage: x is not y
    # x = 10
    # y = 14
    # print(x is y)
    # print(x is not y)

# Python membership opeators
     # in,returns a boolean, usage: x in y
     # not in ,returns a boolean, usage: x not in y

# Python bitwise operators are used to compare binary numbers


print( 4 < 5 and 8 > 5 )
print( 4 < 5 & 8 > 5 )
print( 8 > 5)
    
