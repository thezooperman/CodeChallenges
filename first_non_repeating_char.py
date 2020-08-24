"""
First non-repeating character in a stream

Given an input stream of N characters consisting only of
lower case alphabets. The task is to find the first non
repeating character, each time a character is inserted to
the stream. If no non repeating element is found print -1.

Example:
Input:
2
4
a a b c
3
a a c

Output:
a -1 b b
a -1 c

Explanation:
Test Case 1: a a b c
The step wise first non-repeating elements are made bold:
a (print a)
a a (no non-repeating element, print -1)
a a b (print b)
a a b c (print b)
Result: a -1 b b

Test Case 2: a a c
a (print a)
a a (no non-repeating element, print -1)
a a c (print c)
Result: a -1 c
"""

#code

def driver():
    # testCase = int(input().strip())
    testCase = 1

    for tc in range(testCase):
        noInputs = 4 # int(input().strip())
        array = ['a', 'a', 'b', 'c'] # input().rstrip().split(None)

        charArray = [0] * 26
        j = 0
        for i in range(noInputs):
            charArray[ord(array[i]) - 97] += 1
            while j < i and charArray[ord(array[j]) - 97] != 1:
                j += 1
            if charArray[ord(array[j]) - 97] == 1:
                print(array[j], sep=' ', end=' ')
            else:
                print(-1, sep=' ', end=' ')

        print(flush=True)

if __name__ == "__main__":
    driver()
