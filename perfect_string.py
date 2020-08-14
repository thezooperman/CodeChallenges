"""
    Given a string, find out whether it is Perfect String
    or not. Perfect String here is a String which has the same
    frequency of characters or after performing 1 deletion, the
    frequencies become same. Ex. aabb, aabbc, ababd are perfect
    strings. aabbbc, abcddee are not
    Raises:
        ValueError: [Bad String]

    Returns:
        [bool]: [True is result is true, else False]
"""

from collections import Counter

def check_freq(freq):
    first_freq = 0

    for k,v in freq.items():
        if v > 0:
            first_freq = v
            break
    
    for k,v in freq.items():
        if v > 0 and v != first_freq:
            return False
    
    return True

def perfect_string(string: str) -> bool:
    if not string or len(string) == 0:
        raise ValueError("Bad string!")
    
    # store the frequency
    freq = Counter(string)

    d = dict(freq)

    # check if the freq values are same
    if check_freq(d):
        return True
    
    for k in d.keys():
        # remove freq by 1 and check
        d[k] -= 1
        if check_freq(d):
            return True
        d[k] += 1
    
    return False

if __name__ == "__main__":
    print(perfect_string("abc")) # True
    print(perfect_string("ababd")) # True
    print(perfect_string("abcddee")) # False
