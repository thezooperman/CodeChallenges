from collections import deque
def isBalanced(s):
    stack = deque()
    open_brackets = ['(', '{', '[']
    close_brackets = [')', '}', ']']
    bracket_map = {
        ')': '(',
        ']' : '[',
        '}': '{'
    }
    for bracket in s:
        if bracket in open_brackets:
            stack.append(bracket)
        elif bracket in close_brackets:
            # check if pair is correct
            if not stack or bracket_map.get(bracket) != stack.pop():
                return 'NO'
    if len(stack) == 0:
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    print(isBalanced('}][}}(}][))]')) # should return NO
    print(isBalanced('[](){()}')) # should return YES
    print(isBalanced('({}([][]))[]()')) # should return YES
    print(isBalanced('()')) # should return YES
    print(isBalanced('{)[](}]}]}))}(())(')) # should return NO
    print(isBalanced('([[)')) # should return NO
    # print(isBalanced('(()')) # should return NO
    # print(isBalanced('[[]')) # should return NO
    # print(isBalanced('{{}')) # should return NO
