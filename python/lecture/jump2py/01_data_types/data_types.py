# ANSI ESCAPE CODE
FG_BLACK = "\033[90m"
FG_RED = "\033[91m"
FG_GREEN = "\033[92m"
FG_YELLOW = "\033[93m"
FG_BLUE = "\033[94m"
FG_MAGENTA = "\033[95m"
FG_CYAN = "\033[96m"
FG_WHITE = "\033[97m"
BG_BLACK = "\033[100m"
BG_RED = "\033[101m"
BG_GREEN = "\033[102m"
BG_YELLOW = "\033[103m"
BG_BLUE = "\033[104m"
BG_MAGENTA = "\033[105m"
BG_CYAN = "\033[106m"
BG_WHITE = "\033[107m"
RESET = "\033[0m"

# NUMERIC DATA TYPE
# INTEGER, FLOAT, OCTAL, HEXADECIMAL, BINARY, COMPLEX
print(FG_RED + "NUMERIC DATA TYPE" + RESET)

# INTEGER
integer = 10
print(integer)

# FLOAT
# e or E
float =  4.24E10 # 4.24 * 10^10
print(float)
float = 4.24e-10 # 4.24 * 10^-10
print(float)

# OCTAL
octal = 0o10
print(octal)
octal = 0O10
print(octal)

# HEXADECIMAL
hexadecimal = 0x10
print(hexadecimal)
hexadecimal = 0X10
print(hexadecimal)

# BINARY
binary = 0b10
print(binary)
binary = 0B10
print(binary)

# COMPLEX
complex = 1 + 2j
print(complex)
complex = 1 + 2J
print(complex)

# ~NUMERIC DATA TYPE

# OPERATOR
# +, -, *, /, %, **, //
print(FG_YELLOW + "OPERATOR" + RESET)

# ADDITION
addition = 10 + 20
print(addition)

# SUBTRACTION
subtraction = 20 - 10
print(subtraction)

# MULTIPLICATION
multiplication = 10 * 20
print(multiplication)

# DIVISION
division = 20 / 11
print(division)

# MODULUS
modulus = 20 % 11
print(modulus)

# EXPONENT
exponent = 2 ** 3.32
print(exponent)

# FLOOR DIVISION
floor_division = 20 // 11
print(floor_division)

# COMPARISON
# ==, !=, >, <, >=, <=

# ASSIGNMENT
# =, +=, -=, *=, /=, %=, **=, //=

# ~OPERATOR

# STRING DATA TYPE
# "Data", 'Data', """Data""", '''Data''', r"Data", R"Data", f"Data", F"Data", b"Data", B"Data"
print(FG_GREEN + "STRING DATA TYPE" + RESET)

# STRING OPERATOR
# +, *, [], [:], in, not in
print("MULTI " * 3)

# LEN
string = "Hello World"
print(len(string))

# INDEX
string = "Hello World"
print(string[0])
print(string[-3])

# SLICING
# [start:end:step] start <= index < end
print(string[0:5])
print(string[:5])
print(string[6:])
print(string[:])

# STRING IS IMMUTABLE
python = "Pithon"
# python[1] = "y" # ERROR
python = python[:1] + "y" + python[2:]
print(python)

# STRING METHOD
# count, find, index, join, upper, lower, lstrip, rstrip, strip, replace, split
string = "Hello World"

# count
# return count of substring
print(string.count("l"))

# find
# return index, if not found return -1
print(string.find("l"))

# index
# return index, if not found return ValueError
print(string.index("l"))

# join
# join string with separator
print(":".join(string))

# upper
print(string.upper())

# lower
print(string.lower())

# lstrip
string = "   Hello World"
print(string.lstrip())

# rstrip
string = "Hello World   "
print(string.rstrip())

# strip
string = "   Hello World   "
print(string.strip())

# replace
print(string.replace("Hello", "Hi"))

# split([separator], [maxsplit])
string = "Life is too short"
print(string.split())

# STRING FORMATTING

print("i eat %d apples" % 3)
print("i eat %s apples" % "five")
number = 3
print("i eat %d apples" % number)
day = "three"
print("i ate %d apples. so i was sick for %s days" % (number, day))

# USING FORMAT METHOD (INDEX)
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))

# USING FORMAT METHOD (KEYWORD)
print("I ate {number} apples. so I was sick for {day} days.".format(number=number, day=day))

# F-STRING
print(f"I ate {number} apples. so I was sick for {day} days.")

# RAW STRING
print(r"C:\Program Files\Python\Python.exe")

# ~STRING DATA TYPE

# LIST DATA TYPE
print(FG_CYAN + "LIST DATA TYPE" + RESET)
list = [1, 2, 3, 4, 5, [6, 7, 8, [9, 10]]]
print(list)
print(list[-1][-1])

# SLICING
print(list[4:7])

# OPERATOR
print([1, 2, 3] + [4, 5, 6])
print([1, 2, 3] * 3)

# LIST IS MUTABLE
list = [1, 2, 3, 4, 5]
list[2] = 33
print(list)
del list[2]
print(list)
del list[1:3]
print(list)

# LIST METHOD
# append, sort, reverse, index, insert, remove, pop, count, extend

# append
list = [1, 2, 3]
list.append(4)
print(list)

# sort
list = [3, 1, 2]
list.sort()
print(list)

# reverse
list = [1, 2, 3]
list.reverse()
print(list)

# index
# return index, if not found return ValueError
list = [1, 2, 3]
print(list.index(2))

# insert([index], [value])
list = [1, 2, 3]
list.insert(1, 4)
print(list)

# remove([value])
list = [1, 2, 3]
list.remove(2)
print(list)

# pop([index])
# return value, if not found return IndexError
list = [1, 2, 3]
print(list.pop())
print(list.pop(1))
print(list)

# count
list = [1, 2, 3, 1, 2, 3]
print(list.count(2))

# extend
# == list + list
list = [1, 2, 3]
list.extend([4, 5])
print(list)

# ~LIST DATA TYPE

# TUPLE DATA TYPE
print(FG_BLUE + "TUPLE DATA TYPE" + RESET)

# TUPLE WITH ONE ELEMENT MUST HAVE COMMA
NOT_TUPLE = (1)
tuple = (1,)
print(type(NOT_TUPLE), type(tuple))

# PARENTHESIS IS OPTIONAL
tuple = 1, 2, 3
print(tuple)

# TUPLE IS IMMUTABLE
tuple = (1, 2, 3, 4, 5)
# tuple[2] = 33 # ERROR 
print(tuple)

# ~TUPLE DATA TYPE

# DICTIONARY DATA TYPE (KEY-VALUE PAIR, HASH)
print(FG_MAGENTA + "DICTIONARY DATA TYPE" + RESET)

# DICTIONARY IS MUTABLE
dictionary = {"name": "John", "age": 30}
dictionary["name"] = "Jane"
print(dictionary)

# ADD ELEMENT
dictionary[0] = "zero"
print(dictionary)

# DELETE ELEMENT
del dictionary[0]
print(dictionary)

# LIST CAN'T BE A KEY
# KEY MUST BE IMMUTABLE
# dictionary = {[1, 2]: "list"} # ERROR
dictionary = {(1, 2): "tuple"}
print(dictionary)

# DICTIONARY METHOD
# keys, values, items, clear, get, in, not in, update

# keys
# return list of keys
dictionary = {"name": "John", "age": 30}
print(dictionary.keys())

# values
print(dictionary.values())

# items
# return tuple of key-value pair
print(dictionary.items())

# clear
dictionary.clear()
print(dictionary)

# get
# return value, if not found return None
# dictionary["not_found"] # ERROR
dictionary = {"name": "John", "age": 30}
print(dictionary.get("name"))

# in
print("name" in dictionary)

# not in
print("name" not in dictionary)

# update
dictionary.update({"name": "Jane", "age": 33})
print(dictionary)

# ~DICTIONARY DATA TYPE

# SET DATA TYPE
print(FG_WHITE + "SET DATA TYPE" + RESET)

# SET IS UNORDERED AND NO DUPLICATE
s = set("hello")
print(s)

# FIND SET

# INTERSECTION
s1 = set([1, 2, 3, 4, 5])
s2 = set([4, 5, 6, 7, 8])
print(s1 & s2)

# UNION
print(s1 | s2)

# DIFFERENCE
print(s1 - s2)
print(s1.difference(s2))

# SET METHOD
# add, update, remove

# add
s = set([1, 2, 3])
s.add(4)
print(s)

# update
s.update([5, 6, 7])
print(s)

# remove
s.remove(7)
print(s)

# ~SET DATA TYPE

# BOOLEAN DATA TYPE
print(FG_RED + "BOOLEAN DATA TYPE" + RESET)

# TRUTHY
# True, 1, "string", [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2, 3: 3}

# FALSY
# False, 0, "", [], (), {}, None

a = [1, 2, 3]
while a:
    print(a.pop())

# ~BOOLEAN DATA TYPE

# VARIABLE
print(FG_YELLOW + "VARIABLE" + RESET)

# MEMORY ADDRESS
var = [1, 2, 3]
print(hex(id(var)))

# PYTHON VARIABLE IS REFERENCE
shallow_copy = var
print(hex(id(shallow_copy)))
if (var is shallow_copy):
    print("var is shallow_copy")

# DEEP COPY

# 1. SLICING
deep_copy = var[:]
print(hex(id(deep_copy)))
if (var is not deep_copy):
    print("var is not deep_copy")

# 2. COPY MODULE
from copy import copy
deep_copy = copy(var)
print(hex(id(deep_copy)))
if (var is not deep_copy):
    print("var is not deep_copy")

# ASSIGNMENT
a, b = ("python1", "life1") # == (a, b) = "python", "life"
print(a, b)

[a, b] = ["python2", "life2"]
print(a, b)

a, b = b, a
print(a, b)

a = b = "python3"
print(a, b)

# ~VARIABLE
