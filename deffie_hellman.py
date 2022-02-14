#!/usr/bin/env python3
############################################################
# Author : Kevin Mukuna
# Date : 02/11/2020
# deffie Hellman Key Exchange Algorithm
# Reason: written out of boredom
# NB : these are written straight from math equations
#       they might or may not be as optimise as possible.
# feel free to contact me if you need explanation on how 
#   manage to transform the maths equation into this python
#   code or if your just need explanation
###########################################################
import random

MODULO = None
BASE = None
ALICE = None
BOB = None

def list_of_prime_numbers(prime_range=1000, array_size=100):
    """
    generating a list of prime numbers
    :returns a sorted list of prime numbers
    NB: i am using a small range of possible for fast processing which
    is somehow insecure. use a big range but please
    note it may take hours if not day to complete depending on the size
    of your range
    change the default value to a big value for a strong DFH
    """
    array_of_prime = []
    while len(array_of_prime) < array_size:
        for num in range(2, prime_range):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    if len(array_of_prime) >= array_size:
                        break
                    if num not in array_of_prime:
                        array_of_prime.append(num)
    return sorted(array_of_prime)


def generate_prime_pq(default_range=25):
    """
    :param default_range: random range for prime 
        number(you may remove this if you want to use standard range from 1 to whatever)
    @return modulo and base (p, q)
    """
   
    p = list_of_prime_numbers()[random.randint(default_range, len(list_of_prime_numbers()) - 1)]
    q = 0
    found = False
    while not found:
        if q > p:
            found = True
        else:
            q = list_of_prime_numbers()[random.randint(2, len(list_of_prime_numbers()) - 1)]

    return p, q

def modulo_and_base():
    """
    updates MODULO and BASE values
    """
    global MODULO, BASE
    MODULO, BASE = generate_prime_pq()

def alice_bob_random_int():
    """
    ALICE(Alice chooses a secret integer ) AND 
    BOB(Bob chooses a secret integer ) CHOOSE A SECRET KEY, RANDOMLY
    """
    global ALICE, BOB
    ALICE = random.randint(25, 100)
    BOB = random.randint(7, 50)

def alice():
    """
    sends Bob A = g**a mod p
    """
    print(f"Alice is random number is {ALICE}")
    return ((BASE**ALICE) % MODULO)

def bob():
    """
    sends Alice B = g**b mod p
    """
    print(f"Bob is random number is {BOB}")
    return ((BASE**BOB) % MODULO)

def alice_compute_key():
    """
    Alice computes s = B**a mod p
    """
    return ((bob()**ALICE) % MODULO)

def bob_compute_key():
    """
    Bob computes s = A**b mod p
    """
    return ((alice()**BOB) % MODULO)

if __name__ == "__main__":
    modulo_and_base()
    alice_bob_random_int()
    print(f"Alice computed key is {alice_compute_key()}")
    print(f"Bob Computed key is {bob_compute_key()}")


