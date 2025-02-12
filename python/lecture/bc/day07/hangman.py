import resource as resource
from replit import clear

# Game status variables
cnt = 0
length = len(resource.answer)
current_guesses = ["_"] * length
res = "".join(current_guesses)


def input_only_alpha():
    data = input("Guess a letter: ")
    while not data.isalpha() or len(data) != 1:
        data = input("Please input only a single alphabet letter: ")
    return data.lower()


# Game main logic
while res != resource.answer and cnt < len(resource.hangman):
    clear()
    print(resource.hangman[cnt])
    print(f"{resource.WHITE_TEXT}{res}{resource.RESET_TEXT}")

    guess = input_only_alpha()
    flag = True

    for i in range(length):
        if guess == resource.answer[i] and resource.answer[i] != current_guesses[i]:
            current_guesses[i] = guess
            flag = False
    if flag:
        cnt += 1
    res = "".join(current_guesses)

# Result Output
if res == resource.answer:
    print(f"{resource.GREEN_TEXT}{resource.answer}{resource.RESET_TEXT}")
else:
    print(f"{resource.RED_TEXT}{resource.answer}{resource.RESET_TEXT}")
