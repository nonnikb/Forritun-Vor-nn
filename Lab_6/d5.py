import random
import string

def get_random_letter():
    letters = string.ascii_letters + string.punctuation
    return letters[random.randint(0, len(letters))]


def encrypt(string):
    encrypted = ""
    for x in string:
        encrypted += x + get_random_letter() + get_random_letter()
    return encrypted


random.seed(int(input("Seed: ")))
s = input("I want to encrypt: ")
enc = encrypt(s)
print(enc)


