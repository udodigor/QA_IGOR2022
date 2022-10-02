import random
import string


def random_number():
    """Generation of random number"""
    return str(random.randint(000000, 999999))


def random_str(lenght=5):
    """Generate random string"""
    return ''.join(random.choice(string.ascii_letters) for _ in range(lenght))
