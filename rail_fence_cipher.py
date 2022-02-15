#!/usr/bin/env python
############################################################
# Author : Kevin Mukuna
# Date : 27/09/2021
# Rail fence cipher encryption
# Reason: written out of boredom
# NB : these are written straight from math equations
#       they might or may not be as optimise as possible.
# feel free to contact me if you need explanation on how
#   manage to transform the maths equation into this python
#   code or if your just need explanation.
###########################################################

def enciphering(string_input, fence_depth=3):
    """
    converts plain text to cipher text

    uses transposition with the depth of 3 in this case to
    encrypt messages
    """
    plain_text = (string_input.replace(" ", "")).lower()
    matrix = []
    for each in range(fence_depth):
        matrix.append(["." for _ in range(len(plain_text))])
    depth = 0
    index_of_letter = 0
    up_down = True
    for each_letter in plain_text:
        if up_down:
            matrix[depth][index_of_letter] = each_letter
            depth += 1
            if depth > fence_depth - 1:
                depth -= 2
                up_down = False
        else:
            matrix[depth][index_of_letter] = each_letter
            depth -= 1
            if depth - 1 < 0:
                up_down = True
        index_of_letter += 1

    return matrix


def deciphering(string_input, depth=3):
    pass


def enciphered_message(ciphered_text):
    message = ""
    for each_list in ciphered_text:
        for each_character in each_list:
            if each_character != ".":
                message += each_character
    return message.upper()


if __name__ == "__main__":
    input_string = "meet me at the toga party".replace(" ", "")
    cipher = enciphered_message(ciphered_text=enciphering(string_input=input_string))
    print(cipher)
