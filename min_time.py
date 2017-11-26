'''
Given 6 digits [range 0..9], find the minimum time
that can be generated from the digits
'''
import itertools
import datetime

def mintime(A, B, C, D, E, F):
    '''Given 6 digits, return minimum time in HH MM SS format
        Args:
                \rA : int [0..9]
                \rB : int [0..9]
                \rC : int [0..9]
                \rD : int [0..9]
                \rE : int [0..9]
                \rF : int [0..9]
    '''
    timeformat = "%H:%M:%S"
    valid_time = []
    for p in itertools.permutations([A, B, C, D, E, F]):
        str_time = '{}{}:{}{}:{}{}'.format(*p)
        try:
            datetime.datetime.strptime(str_time, timeformat)
        except ValueError:
            pass
        else:
            valid_time.append(str_time)
    return min(valid_time) if valid_time else 'NOT POSSIBLE'

print(mintime(7, 0, 8, 9, 0, 0)) #returns 07:08:09
print(mintime(0, 0, 8, 9, 0, 0)) #returns 00:08:09
print(mintime(0, 0, 0, 9, 0, 0)) #returns 00:00:09
print(mintime(9, 8, 7, 6, 4, 2)) #returns NOT POSSIBLE
