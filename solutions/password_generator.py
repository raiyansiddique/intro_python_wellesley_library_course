# Create a program that generates strong, random passwords for the user. 
# The program should allow the user to specify the length and complexity 
# of the password.

import random
import string

def generate_password(length):
    """
    Generate a random password of the given length.

    Arguments:
    length -- the length of the password to generate

    Returns:
    A string containing a random password.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Example usage: generate a password of length 10
password = generate_password(10)
print(password)

