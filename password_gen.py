import string
import secrets
# import logging


def genpassord(size=8, chars=string.ascii_letters + string.punctuation
               + string.digits):
    '''Password generation basic rule'''
    return ''.join([secrets.choice(chars) for _ in range(size)])


def get_password(size=8, digits=False, special_chars=False, capital=False):
    result = []
    final_literal = {}
    counter = 0
    final_literal[counter] = string.ascii_lowercase

    if digits:
        counter += 1
        final_literal[counter] = string.digits
    if special_chars:
        counter += 1
        final_literal[counter] = '!_#@*:?^|~-+$'
    if capital:
        counter += 1
        final_literal[counter] = string.ascii_uppercase

    keys = [_ for _ in range(len(final_literal))]
    for _ in range(size):
        # out of final_literal, pick one set at random
        r_group = secrets.choice(keys)
        print(f'Group: {r_group}')
        r_choice = secrets.choice(final_literal[r_group])
        # possibly introduce an option to hydrate a group
        final_literal[r_group] = final_literal[r_group].replace(r_choice, '')
        result.append(r_choice)
    return ''.join(result)


# print(genpassord(size=int(input('How many characters in password?').strip())))

size = int(input('How many characters in password?').strip())
digits = bool(input('Need digits? (y/n)').strip() != 'n')
special_chars = bool(input('Need special characters? (y/n)').strip() != 'n')
capital = bool(input('Need capital letters? (y/n)').strip() != 'n')
print(get_password(size, digits, special_chars, capital))
# duplicate = {}
# for i in range(100):
#     passwd = get_password(size, digits, special_chars, capital)
#     print(passwd)
#     if passwd not in duplicate:
#         duplicate[i] = passwd
#     else:
#         logging.critical(f'Duplicate password : {passwd}')
