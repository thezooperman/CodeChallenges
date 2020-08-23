"""
Find next greater number with same set of digits

Given a number n, find the smallest number that has
same set of digits as n and is greater than n. If n
is the greatest possible number with its set of digits,
then print “not possible”.
Examples:
For simplicity of implementation, we have considered input
number as a string.

Input:  n = "218765"
Output: "251678"

Input:  n = "1234"
Output: "1243"

Input: n = "4321"
Output: "Not Possible"

Input: n = "534976"
Output: "536479"
"""

# 1. Iterate from last
# 2. find the first number < current number
# 3. from that number index, find the number immediately greater
# 4. on right
# 5. swap the position - step 2 and 3
# 6. sort the remaining value from 3 till n
# that is the answer


def next_largest(n: list):
   last_digit = n[-1]

   for i in range(len(n) - 2, -1, -1):
       if last_digit > n[i]:
           break
       last_digit = n[i]

   if i >= 0:
       for j in range(len(n) - 1, i, -1):
           if n[j] > n[i]:
               break
       n[j], n[i] = n[i], n[j]
       s = sorted(n[i + 1:])
       n = n[:i + 1] + s

   return n
    


if __name__ == "__main__":
    print(*next_largest([5,3,4,9,7,6])) # 536479
    print(*next_largest([1,2,3,4])) # 1243
    print(*next_largest([6,9,3,8,6,5,2])) # 6952368
    print(*next_largest([4,7])) # 74
    print(*next_largest([1,3,2])) # 213
    print(*next_largest([2,3,5,4])) # 2435
