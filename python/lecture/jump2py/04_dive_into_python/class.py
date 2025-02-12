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

# Why do we need classes?
# Example: calculator
res = 0

def add(num):
    global res
    res += num
    return res

print(add(3))
print(add(4))

# If we want to use two calculators at the same time, we need to create two separate variables
res1 = 0
res2 = 0

def add1(num):
    global res1
    res1 += num
    return res1

def add2(num):
    global res2
    res2 += num
    return res2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(4))

# Classes allow us to create multiple instances of the same object
# class ClassName:
#     def __init__(self, parameters, ...):
#         self.attribute = value
#
#     def method_name(self, parameters, ...):

class Calculator:
    def __init__(self):
        self.res = 0

    def add(self, num):
        self.res += num
        return self.res

calc1 = Calculator()
calc2 = Calculator()

print(calc1.add(3))
print(calc1.add(4))
print(calc2.add(3))
print(calc2.add(4))

# Pass 
class EmptyClass:
    pass

a = EmptyClass()

print(type(a))

class Calculator:
    def set_data(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        return self.first + self.second

a = Calculator()
a.set_data(4, 5)
print(a.first, a.second)

# Another way to call a method
# ClassName.method_name(instance, parameters, ...)
Calculator.set_data(a, 4, 5)
print(a.add())

# __init__ method(Constructor)
a = Calculator()
# a.add() # Error

class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def set_data(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        return self.first + self.second

a = Calculator(4, 5)
print(a.add())

# Inheritance
# class DerivedClassName(BaseClassName):

class MoreCalculator(Calculator):
    def subtract(self):
        return self.first - self.second
    def divide(self):
        return self.first / self.second

a = MoreCalculator(4, 5)
print(a.subtract())

# Overriding methods
class SafeMoreCalculator(MoreCalculator):
    def divide(self):
        if self.second == 0:
            return f"{FG_RED}Error: Division by zero{RESET}"
        else:
            return self.first / self.second

a = SafeMoreCalculator(4, 0)
print(a.divide())
a = MoreCalculator(4, 0)
# print(a.divide()) # Error

# Class attributes
# in C++, static member variables
class Family:
    last_name = "Simpson"

a = Family()
b = Family()
print(a.last_name)
print(b.last_name)

# Overriding class attributes
a.last_name = "Smith"
print(a.last_name)
print(b.last_name)
