import random

print("Welcome to the PyPassword Generator")
letters = int(input("How may letters would you like in your password?"))

digits = "0123456789"
lowers = "abcdefghijklmnopqrstuvwxyz"
uppers = lowers.upper()
specials = "!@#$%^&*_+-="
words = digits + lowers + uppers + specials

pw = ""

for i in range(0, letters):
    # idx = random.randint(0, len(words) - 1)
    # pw += words[idx]
    char = random.choice(words)
    pw += char

print(f"Your password is: {pw}")
