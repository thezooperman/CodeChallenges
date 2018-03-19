'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output,
#  will cause the test cases to fail
'''

N = int(input().strip())

for it in range(N):
    S = input().strip()
    length = len(S)
    isPalindrome = True
    for i in range(length // 2):
        if S[i] != S[length - i - 1]:
            isPalindrome = False
            break
    if isPalindrome:
        if length % 2 == 0:
            print('YES EVEN')
        else:
            print('YES ODD')
    else:
        print('NO')
