#!/usr/bin/env python
############################################################
# Author : Kevin Mukuna
# Date : 27/09/2021
# Caesar Cipher
# Reason: written out of boredom
###########################################################

import string


def alphabet():
    """
    returns a list of the 26 alphabet letters
    """
    return [_ for _ in string.ascii_lowercase]


def string_chunks(string_input, chunks=4):
    """
    :param string_input: input text string
    :param chunks: slice your string chunks of 4
    returns list of blocks of 4s
    """
    return [string_input[i:i + chunks] for i in range(0, len(string_input), chunks)]


def enciphering(string_input):
    """
    converts plain text to cipher text

    iterates over each letter and shift it by 4 space
    producing unique character in each index position in
    a string
    """

    plain_ = string_chunks(string_input)
    alpha = alphabet()
    cipher_result = ""
    for each_block in plain_:
        for each_letter in each_block:
            letter_index = alpha.index(each_letter)
            if letter_index > 22:
                temp = letter_index + 4
                cipher_index = temp - 25
                cipher_result += alpha[cipher_index]
            else:
                letter_index += 4
                cipher_result += alpha[letter_index]
    return cipher_result


def deciphering(string_input):
    """converts cipher text back to plain text """
    plain_ = string_chunks(string_input)
    alpha = alphabet()
    text_result = ""
    for each_block in plain_:
        for each_letter in each_block:
            letter_index = alpha.index(each_letter)
            if letter_index < 4:
                temp = letter_index - 5
                text_result += alpha[temp]
            else:
                text_result += alpha[letter_index - 4]
    return text_result


def main(default="MEET ME AFTER THE TOGA PARTY"):
    original = (default.replace(" ", "")).lower()
    enciphering_result = enciphering(original)
    deciphering_result = (deciphering(enciphering_result))
    if original == deciphering_result:
        print("caesar cipher algorithm")
    else:
        print(f"original string: {original}")
        print(f"cipher result: {enciphering_result}")
        print(f"decipher result : {deciphering_result}")


if __name__ == "__main__":
    main()
