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

# If Conditional Statement
print(FG_RED + "IF CONDITIONAL STATEMENT" + RESET)

age = 18
if age >= 18:
    print("You are eligible to vote.")
elif age < 18:
    print("You are not eligible to vote.")
else:
    print("Invalid age.")

# x && y -> x and y
# x || y -> x or y
# !x -> not x

# in, not in
# x in list -> True if x is in list
# x in tuple -> True if x is in tuple
# x in string -> True if x is in string

list = [1, 2, 3, 4, 5]
if 3 in list:
    print("3 is in the list.")

py = "Python"
if "j" not in py:
    print("j is not in Python.")

# Conditional Expression
# res = x if condition else y (Python)
# res = condition ? x : y (C, C++)
score = 80
result = "Pass" if score >= 40 else "Fail"
print(result)

# ~If Conditional Statement

# Looping Statements
print(FG_YELLOW + "LOOPING STATEMENTS" + RESET)

# while loop
i = 0
while i < 5:
    print(i, end=" ")
    i += 1
print()

# continue statement
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# break statement
i = 0
while True:
    print(i, end=" ")
    i += 1
    if i == 5:
        break

# Infinite Loop
# while True:
#     print("Infinite Loop")

# for loop
list = ["Python", "Java", "C++", "C", "JavaScript"]
for lang in list:
    print(lang, end=" ")
print()

tuple_list = [(1, 2), (3, 4), (5, 6)]
for (a, b) in tuple_list:
    print(a, b)

# range(start, stop, step)
for i in range(10):
    print(i, end=" ")
print()

for i in range(5, 10):
    print(i, end=" ")
print()

for i in range(0, 10, 2):
    print(i, end=" ")
print()

# List Comprehension
# [expression for item in list [if condition]]
list = [1, 2, 3, 4, 5]
result = []
for i in list:
    result.append(i * i)
print(result)

list = [1, 2, 3, 4, 5]
result = [i * i for i in list if i % 2 == 0]
print(result)

# [expression for item1 in list1 [if condition1]
            # for item2 in list2 [if condition1]
            # for item3 in list3 [if condition1]
            # for item4 in list4 [if condition1]]

times_table = [(i, j, i * j) for i in range(2, 10) 
                            for j in range(1, 10)]

for (i, j, k) in times_table:
    print(f"{i} x {j} = {k}")
