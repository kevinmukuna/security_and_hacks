#!/usr/bin/env python
############################################################
# Author : Kevin Mukuna
# Date : 27/09/20221
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
            depth -=1
            if depth - 1 < 0:
                up_down = True
        index_of_letter += 1

    for each_list in matrix:
        print(each_list)


if __name__ == "__main__":
    input_string = "meet me at the toga party".replace(" ", "")
    enciphering(string_input=input_string)
