def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")
# greet()

# name: Parameter
# "Seunan": Argument
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print("Isn't the weather nice today?")
# greet_with_name("Seunan")

# Impossible function overloading in Python
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"Isn't the weather nice today in {location}?")

greet_with("Seunan", "Seoul")
# Use keyword arguments to avoid confusion
# But length of code will be longer
greet_with(location="Seoul", name="Seunan")
