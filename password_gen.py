import string
import random


def genpassord(size=8, chars=string.ascii_letters + string.punctuation
               + string.digits):
    '''Password generation basic rule'''
    return ''.join([random.choice(chars) for _ in range(size)])


print(genpassord(size=int(input('How many characters in password?').strip())))
