ALPHABET_COUNT = 26

RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
WHITE = "\033[0;37m"
RESET = "\033[0m"

def input_valid_direction():
    direction = input(f"{WHITE}Type 'encode' to encrypt, type 'decode' to decrypt:\n{RESET}")
    while direction not in ["encode", "decode"]:
        direction = input(f"{YELLOW}Invalid input. Please type 'encode' to encrypt, type 'decode' to decrypt:\n{RESET}")
    return direction

def can_convert_to_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def input_valid_shift():
    shift = input(f"{WHITE}Type the shift number (as an integer):\n{RESET}")
    while not can_convert_to_int(shift):
        shift = input(f"{YELLOW}Invalid input. Please type the shift number (as an integer):\n{RESET}")
    return int(shift)
    
def shift_char(char, shift, direction):
    effective_shift = shift % ALPHABET_COUNT 
    if direction == "left":
        effective_shift = -effective_shift
    new_char_ord = ord(char) + effective_shift
    if new_char_ord > ord('z'): 
        new_char_ord -= ALPHABET_COUNT
    elif new_char_ord < ord('a'):
        new_char_ord += ALPHABET_COUNT
    return chr(new_char_ord)

direction = input_valid_direction()
text = input(f"{WHITE}Type your message:\n{RESET}").lower()
shift = input_valid_shift()

def caesar_cipher(text, shift, direction):
    result_text = ""
    for char in text:
        if char.isalpha():
            result_text += shift_char(char, shift, direction)
        else:
            result_text += char
    print(GREEN + result_text + RESET)

if (direction == "encode"):
    caesar_cipher(text, shift, "right")
elif (direction == "decode"):
    caesar_cipher(text, shift, "left")
