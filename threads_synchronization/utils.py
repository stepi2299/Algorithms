import random

def generate_even_number():
    return random.randint(0, 20) * 2


def generate_odd_number():
    return random.randint(0, 20) * 2 + 1