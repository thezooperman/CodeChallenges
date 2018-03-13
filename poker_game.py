# poker_game.py
'''
Given a game of poker hands, find out
which hand wins the game. If right hand wins,
print `right`, else print `left`. If there is a
draw, print `none`
Sample Input - TD 9S 8H 7D 6C 6S 6H 6D KC KH
Explanation - TD 9S 8H 7D 6C|6S 6H 6D KC KH
Each hand has a total of 5 cards, the input is
arranged accordingly and the cards are separated by
a space.
Output - right

Sample Input - TD JD QD KD AD 8C AC AD AH AS
Output - left

All the regular rules of Poker applies
https://en.wikipedia.org/wiki/List_of_poker_hands
'''

# import sys
from collections import defaultdict

# card_order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
#               '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
card_order = {}


def init_card_order():
    global card_order
    card_order = {str(i): i for i in range(2, 10)}
    card_order['T'] = 10
    card_order['J'] = 11
    card_order['Q'] = 12
    card_order['K'] = 13
    card_order['A'] = 14
    # print(card_order)


def check_flush(hand):
    suits = [h[1] for h in hand]
    if len(set(suits)) == 1:
        return True
    else:
        return False


def check_straight_flush(hand):
    if check_flush(hand) and check_straight(hand):
        return True
    else:
        return False


def check_four_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [1, 4]:
        return True
    return False


def check_full_house(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [2, 3]:
        return True
    return False


def check_straight(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    rank_values = [card_order[i] for i in values]
    value_range = max(rank_values) - min(rank_values)
    if len(set(value_counts.values())) == 1 and (value_range == 4):
        return True
    else:
        # check straight with low Ace
        if set(values) == set(["A", "2", "3", "4", "5"]):
            return True
        return False


def check_three_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if set(value_counts.values()) == set([3, 1]):
        return True
    else:
        return False


def check_two_pairs(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [1, 2, 2]:
        return True
    else:
        return False


def check_one_pairs(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if 2 in value_counts.values():
        return True
    else:
        return False


def check_royal_flush(hand):
    values = [i[0] for i in hand]
    rank_values = [card_order[i] for i in values]
    if sorted(rank_values) == [10, 11, 12, 13, 14] and check_flush(hand):
        return True
    else:
        return False


def check_hand(hand):
    if check_royal_flush(hand):
        return 10
    if check_straight_flush(hand):
        return 9
    if check_four_of_a_kind(hand):
        return 8
    if check_full_house(hand):
        return 7
    if check_flush(hand):
        return 6
    if check_straight(hand):
        return 5
    if check_three_of_a_kind(hand):
        return 4
    if check_two_pairs(hand):
        return 3
    if check_one_pairs(hand):
        return 2
    return 1


init_card_order()
# for line in sys.stdin:
line = input('Input left and right hand cards:')
temp_arr = line.split(' ')
left_hand, right_hand = temp_arr[:5], temp_arr[5:]
right_hand[-1] = right_hand[-1].replace('\n', '')
# get left hand card value
left_hand_value = check_hand(left_hand)
# get right hand card value
right_hand_value = check_hand(right_hand)

if int(left_hand_value) > int(right_hand_value):
    print('left')
elif int(left_hand_value) < int(right_hand_value):
    print('right')
else:
    print('none')
