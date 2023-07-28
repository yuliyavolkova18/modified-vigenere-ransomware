#!/usr/bin/env python3

"""
Modified vigenere cipher 
encryption and decryption logic
"""

def initialize_variables():
    index = 0
    text = ""
    space = chr(32)  # Lowest ASCII character used
    range_length = ord('~') - ord(' ') + 1  # Range of usable ASCII characters
    return index, text, space, range_length


def encrypt_vigenere(plaintext, key):
    index, ciphertext, space, range_length = initialize_variables()

    for i in range(len(plaintext)):
        char = plaintext[i]

        if char == '\n':
            ciphertext += char
            continue

        # Get ASCII value of each char of the key adjusted to the beginning of the usable ASCII value bound
        offset = ord(key[index]) - ord(space)

        # Convert each char of the message and adjust to the Vigenère cipher matrix and usable ASCII value bound
        string_char = str(char)
        ASCII_value = (ord(string_char) - ord(space) + offset) % range_length
        ciphered_char = chr(ASCII_value + ord(space))
        ciphertext += ciphered_char

        # Continue generating key chars in a loop, excluding newlines
        while plaintext[index] == '\n':
            index = (index + 1) % len(plaintext)
        index = (index + 1) % len(key)

    return ciphertext


def decrypt_vigenere(ciphertext, key):
    index, plaintext, space, range_length = initialize_variables()

    for i in range(len(ciphertext)):
        char = ciphertext[i]

        if char == '\n':
            plaintext += char
            continue

        # Get ASCII value of each char of the key adjusted to the beginning of the usable ASCII value bound
        key_offset = ord(key[index]) - ord(space)

        # Calculate the positive offset based on the corresponding key character
        positive_offset = range_length - (key_offset % range_length)

        # Calculate the modular arithmetic taking into account the range of usable ASCII characters
        cipher_value = (ord(char) - ord(space) + positive_offset) % range_length
        plain_char = chr(cipher_value + ord(space))
        plaintext += plain_char

        # Continue generating key chars in a loop, excluding newlines
        while ciphertext[index] == '\n':
            index = (index + 1) % len(ciphertext)
        index = (index + 1) % len(key)

    return plaintext
