# ANSI escape codes
FG_BLACK = '\033[90m'
FG_RED = '\033[91m'
FG_GREEN = '\033[92m'
FG_YELLOW = '\033[93m'
FG_BLUE = '\033[94m'
FG_MAGENTA = '\033[95m'
FG_CYAN = '\033[96m'
FG_WHITE = '\033[97m'
BG_BLACK = '\033[100m'
BG_RED = '\033[101m'
BG_GREEN = '\033[102m'
BG_YELLOW = '\033[103m'
BG_BLUE = '\033[104m'
BG_MAGENTA = '\033[105m'
BG_CYAN = '\033[106m'
BG_WHITE = '\033[107m'
REGULAR = '\033[0m'
BOLD = '\033[1m'
FAINT = '\033[2m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
BLINK = '\033[5m'
RAPID_BLINK = '\033[6m'
NEGATIVE = '\033[7m'
HIDDEN = '\033[8m'
STRIKE_THROUGH = '\033[9m'
RESET = '\033[0m'
# ~ANSI escape codes

# Function
# def function_name(parameters, ...):
    # code
    # ...
    # return value

# Call function
# function_name(arguments, ...)
def print_color(color, message):
    print(color + message + RESET)

print_color(FG_RED, "Function")

# Set parameters
def func(name, age):
    print(f"My name is {name} and I am {age} years old.")

func(age=25, name="John")

# Default parameters
# default value should be set rightmost
def func(name="John", age=25):
    print(f"My name is {name} and I am {age} years old.")

func()

# *(asterisk) operator
def func(*args):
    res = 0
    for i in args:
        res += i
    print(res)

func(1, 2, 3, 4, 5)
func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def calc(operator, *args):
    res = 0
    if operator == "+":
        for i in args:
            res += i
    elif operator == "*":
        res = 1
        for i in args:
            res *= i
    print(res)

calc("+", 1, 2, 3, 4, 5)
calc("*", 1, 2, 3, 4, 5)

# **(double asterisk) operator (keyword arguments)
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(name="John", age=25, city="New York")

# Parameter is not referenced
def not_referenced(param):
    param = 100

a = 10
not_referenced(a)
print(a)

# Global
a = 1
def set_variable():
    global a
    a = 100

set_variable()
print(a)

# Lambda function
# function_name = lambda parameters, ...: expression
add = lambda x, y: x + y 
# == def add(x, y):
#        return x + y
res = add(1, 2)
print(res)
# ~Function

# User input/output
print_color(FG_YELLOW, "USER IO")

# input([Message])
# returns string that user entered
num = input("Enter a number: ")
print(num)

# print([Message], ..., [sep=' '], [end='\n'])
# prints message to the screen
print("Life", "is", "short")
print("Life" + " is " + "short")
print("Life", "is", "short", end=".")
print("Life", "is", "short", sep="\n")
# ~User input/output

# File input/output
print_color(FG_GREEN, "FILE IO")

# open(file, mode)
# file: file path
# mode: r(read), w(write), a(append), x(create)
# returns file object
file = open("file.txt", "w")
for i in range(10):
    data = f"{i + 1} line\n"
    file.write(data)
file.close()

# readline
# returns one line from the file
file = open("file.txt", "r")
while True:
    line = file.readline()
    if not line:
        break
    print(line, end="")
file.close()

# readlines
# returns list of all lines in the file
file = open("file.txt", "r")
lines = file.readlines()
for line in lines:
    print(line, end="")
file.close()

# read
# returns all lines in the file as a string
file = open("file.txt", "r")
data = file.read()
print(data, end="")
file.close()

# for loop with file object
f = open("file.txt", "r")
for line in f:
    print(line, end="")
f.close()

# append
f = open("file.txt", "a")
for i in range(10):
    data = f"{i + 11} line\n"
    f.write(data)
f.close()

# with statement
# automatically closes the file
with open("file.txt", "r") as f:
    for line in f:
        print(line, end="")
# closes the file automatically

# Delete file
import os
os.remove("file.txt")
# ~File input/output

# Program arguments
print_color(FG_BLUE, "PROGRAM ARGUMENTS")

# sys.argv
# returns list of arguments
import sys

print(sys.argv[1:])
# ~Program arguments
