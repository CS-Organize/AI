############DEBUGGING#####################

# Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

"""
1. 코드의 흐름을 따라가면서 문제를 파악한다.

range(1, 20)는 (int i = 1; i < 20; i++)과 같은 의미이다.
따라서 i는 1부터 19까지 증가하게 되고, i == 20이 되는 경우는 없다.
"""

# Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# # dice_num = 6
# print(dice_imgs[dice_num])

"""
2. 문제를 재현한다.

Traceback (most recent call last):
  File "/Users/anseungwon/dev/Python/bootCamp/day13/bug.py", line 21, in <module>
    print(dice_imgs[dice_num])
          ~~~~~~~~~^^^^^^^^^^
IndexError: list index out of range

언제 IndexError가 발생하는지 파악한다.
"""

# Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
# elif year >= 1994: #answer
#   print("You are a Gen Z.")

"""
3. 본인이 컴퓨터라고 가정하고 코드를 읽어본다.
"""

# Fix the Errors
# age = input("How old are you?")
# age = int(input("How old are you?")) #answer
# if age > 18:
# print("You can drive at age {age}.")

"""
4. 문제를 해결한다.

에러 메시지를 보고 어떤 문제가 있는지 파악한다.
구글링 혹은 GPT를 활용하여 문제를 해결한다.
"""

# Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) # fix "==" to "="
# print(pages, word_per_page)
# total_words = pages * word_per_page
# print(total_words)

"""
5. print()를 활용하여 문제를 파악한다.

간단한 문제는 print()를 활용하여 문제를 파악한다.
복잡한 문제는 디버거를 활용한다.
"""


# Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])

"""
6. 디버거를 활용하여 문제를 파악한다.
"""

"""
7. 충분한 휴식을 취하고, 다시 코드를 읽어본다.
8. 다른 사람에게 코드를 리뷰받는다.
9. 코드를 자주 실행하고, 테스트한다.
"""
