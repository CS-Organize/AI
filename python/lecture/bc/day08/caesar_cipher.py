ALPHABET_COUNT = 26

def input_valid_direction():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    while (direction != "encode" and direction != "decode"):
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    return direction

def can_convert_to_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def input_valid_shift():
    shift = input("Type the shift number (as an integer):\n")
    while not can_convert_to_int(shift):
        shift = input("Invalid input. Please type the shift number (as an integer):\n")
    return int(shift)

def shift_right(char, shift):
    real_shift = shift % ALPHABET_COUNT
    if ord(char) + real_shift > ord('z'):
        return chr(ord(char) + real_shift - ALPHABET_COUNT)
    else:
        return chr(ord(char) + real_shift)

def shift_left(char, shift):
    real_shift = shift % ALPHABET_COUNT
    if ord(char) - real_shift < ord('a'):
        return chr(ord(char) - real_shift + ALPHABET_COUNT)
    else:
        return chr(ord(char) - real_shift)

direction = input_valid_direction()
text = input("Type your message:\n").lower()
shift = input_valid_shift()

def encode():
    encoded_text = ""
    for char in text:
        if char.isalpha():
            encoded_char = shift_right(char, shift)
            encoded_text += encoded_char
        else:
            encoded_text += char
    print(encoded_text)

def decode():
    encoded_text = ""
    for char in text:
        if char.isalpha():
            encoded_char = shift_left(char, shift)
            encoded_text += encoded_char
        else:
            encoded_text += char
    print(encoded_text)

if (direction == "encode"):
    encode()
elif (direction == "decode"):
    decode()
