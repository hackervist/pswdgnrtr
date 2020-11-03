import string
import random


def password(length, num=False, strength='weak'):
    """Length of password, num if you want a number, 
    and strenth (weak. strong, very strong"""
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    letter = lower + upper
    dig = string.digits
    punc = string.punctuation
    pwd = ''
    if strength == 'weak':
        if num:
            length -= 2
            for i in range(2):
                pwd += random.choice(dig)
        for i in range(length):
            pwd += random.choice(lower)

    elif strength == 'strong':
        if num:
            length -= 2
            for i in range(2):
                pwd += random.choice(dig)

        for i in range(length):
            pwd += random.choice(letter)
    elif strength == 'very':
        ranNums = random.randint(2, 4) # random amount of numbers 
        ranPunc = random.randint(2, 4) # random amount of punctuations 
        # print (ranNums)
        if num:
            length -= ranNums
            for i in range(ranNums):
                pwd += random.choice(dig)
            length -= ranPunc 
            for i in range(ranPunc ):
                pwd += random.choice(punc)

        for i in range(length):
            pwd += random.choice(letter)

    pwd = list(pwd)
    random.shuffle(pwd)

    return ''.join(pwd)

# minimum should be 6
print(password(6, True, 'weak'))

print(password(6, True, 'strong'))

print(password(6, False, 'very'))