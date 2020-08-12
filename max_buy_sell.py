'''
Stock Buy Sell to Maximize Profit

The cost of a stock on each day is given in an array,
find the max profit that you can make by buying and
selling in those days. For example, if the given array
is {100, 180, 260, 310, 40, 535, 695}, the maximum profit
can earned by buying on day 0, selling on day 3. Again
buy on day 4 and sell on day 6. If the given array of
prices is sorted in decreasing order, then profit
cannot be earned at all.
'''

from typing import List


def maxProfit(arr: List[int]):
    n = len(arr) - 1

    i = 0

    while (i <= n):
        # local minima
        while (i <= n) and arr[i + 1] <= arr[i]:
            i += 1
        
        if i >= n:
            break

        buy = i
        i += 1
        # local maxima
        while (i <= n) and arr[i] >= arr[i - 1]:
            i += 1

        sell = i - 1
        print(f"Buy on day:{buy}. Sell on day:{sell}")


# Driver code 
if __name__ == '__main__': 
    price = [100, 180, 260, 310, 40, 535, 695]; 
    n = len(price); 
  
    print(maxProfit(price))
