print("Welcome to the 4000 Weeks Calculator")

age = input("\033[0;37mWhat is your current age?\n\033[0m")
while (not age.isdigit()):
  age = input("\033[0;37mWhat is your current age?\n\033[0m")

age = int(age)
weeks = 4000 - age * 52

if (weeks < 0):
  print("\033[0;31mYou have already lived more than 4000 weeks\033[0m")
else:
  print(f"\033[0;37mYou have \033[0;33m{weeks}\033[0;37m weeks left\033[0m")

