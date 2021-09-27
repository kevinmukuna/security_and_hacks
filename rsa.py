#!/usr/bin/env python
############################################################
# Author : Kevin Mukuna
# Date : 02/11/2020
# RSA encryption scheme
# Reason: written out of boredom
# NB : these are written straight from math equations
#       they might or may not be as optimise as possible.
# feel free to contact me if you need explanation on how 
#   manage to transform the maths equation into this python
#   code or if your just need explanation
###########################################################
import random
import string


def list_of_prime_numbers(default_range=100):
    """
    generating a list of prime numbers
    :returns a sorted list of prime numbers

    NB: i am using a small range of possible for fast processing which
    is somehow insecure. how a more RSA use a big range but please
    note it may take hours if not day to complete depending on the size
    of your range

    change the default value for a strong RSA
    """
    array_of_prime = []
    while len(array_of_prime) < 10:
        for num in range(2, default_range):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    if len(array_of_prime) >= 10:
                        break
                    array_of_prime.append(num)
    return sorted(array_of_prime)


def generate_prime_pq():
    """
    generate any 2 prime numbers to represent p and q
    getting any 2 prime numbers in the list of prime numbers where q > p
    """
    p = list_of_prime_numbers()[random.randint(2, len(list_of_prime_numbers()) - 1)]
    q = 0
    found = False
    while not found:
        if q > p:
            found = True
        else:
            q = list_of_prime_numbers()[random.randint(2, len(list_of_prime_numbers()) - 1)]

    return p, q


def corePrimeWithN(n):
    result = [1]
    for i in range(1, n + 1):
        if n % i != 0 and i % 2 != 0:
            result.append(i)
    return result


def drive_function():
    """
    this is the drive code for RSA
    pq_prime: generated prime number p and such that q>p
    ff : fine function result
    e : encryption result
    dec : decryption result
    msg : message returned after encryption
    d_msg : message return after decryption
    """
    pq_prime = generate_prime_pq()
    p = pq_prime[0]
    q = pq_prime[1]
    product = product_of_pq(p, q)
    ff = fine_function(p, q)
    e = encryption_key(p, product, ff)
    dec = decryption_key(e, ff)
    msg = encrypt_message(e, product)
    d_mg = decrypt_message(msg, dec, product)
    return d_mg


def product_of_pq(p, q):
    """returns product of the p and q"""
    return p * q


def fine_function(p, q):
    """takes in the co prime of N (also known as co-prime of the product of p and q)"""
    return (p - 1) * (q - 1)


def encryption_key(p, N, ff):
    """
    generate the encryption key using the fine function and N
    e must between 1 and N(the fine_function)  must be co-prime with N fine-function
    """
    e = 0
    for i in range(p, ff):
        if N % i != 0 and ff % i != 0:
            e = i
    return e


def encrypt_message(e, N):
    """return cypher text as an number using encryption key and the product of p+q"""
    msg = [_ for _ in string.ascii_uppercase]
    text = str(input("enter a text to decrypt : ")).upper()
    index = msg.index(text)
    ciphertext = ((index ** e) % N)
    print(f"sending cipherText as {ciphertext}")
    return ciphertext


def decrypt_message(msg, d_key, p_mod):
    """
    decrypting the message
    """
    x = msg ** d_key
    r = x % p_mod
    return r


def decryption_key(e, ff):
    """condition of the d key is that De(mod fine_function) should equal 1"""
    found = False
    var = e
    deC = 0
    count = 1
    while not found:
        if (var * count) % ff == 1:
            if len(str(count)) >= 2:
                s = [_ for _ in str(count)]
                if str(s[-1]) == "1":
                    deC = count
                    found = True
        # var +=e
        count += 1
    return deC


if __name__ == "__main__":
    count = 0
    while count < 25:
        msg = drive_function()
        var = [_ for _ in string.ascii_uppercase]
        print(var[msg])
        count += 1
