'''
Password generator function
'''
import string
import secrets


def get_password(size=8, digits=False, special_chars=False, capital=False, whitespace=False):
    """
        Generate a random strong password. By default, password will only
        be of lowercase ascii letters, if no other options are set
        Args:
            size:int, length of password, default size is 8
            digits:bool, does the password need digits, default value False
            special_chars:bool, does the password need special characters, default value False
            capital:bool, does the password need capital letters, default valie False 
            whitespace:bool, does the password need whitespace, default value False
    """
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

    keys = list(final_literal.keys())  # [_ for _ in range(len(final_literal))]
    # print(final_literal.keys())
    for _ in range(size):
        # out of final_literal, pick one set at random
        r_group = secrets.choice(keys)
        # print(f'Group: {r_group}')
        r_choice = secrets.choice(final_literal[r_group])
        # possibly introduce an option to hydrate a group
        # final_literal[r_group] = final_literal[r_group].replace(r_choice, '')
        result.append(r_choice)
    if whitespace:
        rand = secrets.SystemRandom()
        if size > 20:
            # get random number of white spaces but < 5
            random_ws = rand.randint(1, 5)
            for _ in range(random_ws):
                random_whitespace_index = rand.randint(1, len(result) - 1)
                result.insert(random_whitespace_index, ' ')
        else:
            random_whitespace_index = rand.randint(1, len(result) - 1)
            result.insert(random_whitespace_index, ' ')
    return ''.join(result)


size = int(input('How many characters in password?').strip())
digits = bool(input('Need digits? (y/n)').strip() != 'n')
special_chars = bool(input('Need special characters? (y/n)').strip() != 'n')
whitespace = bool(input('Need white space? (y/n)').strip() != 'n')
capital = bool(input('Need capital letters? (y/n)').strip() != 'n')

print(get_password(size, digits, special_chars, capital, whitespace))
