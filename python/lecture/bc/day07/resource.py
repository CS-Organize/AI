# ANSI COLOR CODE
RED_TEXT = "\033[0;31m"
GREEN_TEXT = "\033[0;32m"
WHITE_TEXT = "\033[0;37m"
RESET_TEXT = "\033[0m"

# Generate a answer
import requests

url = "https://random-word-api.herokuapp.com/word"
response = requests.get(url)

if response.status_code == 200:
    answer = response.json()[0].lower()
else:
    print("\033[0;31mUnable to load word from API{RESET_TEXT}")
    answer = "apple"  # default word

# Hangman ascii art
hangman = [
    r"""
    ________
    |/      |
    |      
    |      
    |     
    |      
    |
    |___
""",
    r"""
    ________
    |/      |
    |      (_)
    |    
    |     
    |      
    |
    |___
""",
    r"""
    ________
    |/      |
    |      (_)
    |       |
    |       |
    |     
    |
    |___
""",
    r"""
    ________
    |/      |
    |      (_)
    |      \|
    |       |
    |      
    |
    |___
""",
    r"""
    ________
    |/      |
    |      (_)
    |      \|/
    |       |
    |      
    |
    |___
""",
    r"""
    ________
    |/      |
    |      (_)
    |      \|/
    |       |
    |      /
    |
    |___
""",
    r"""
    ________
    |/      |
    |      (_)
    |      \|/
    |       |
    |      / \
    |
    |___
""",
]
