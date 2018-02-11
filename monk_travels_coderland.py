# monk_travels_coderland.py

import sys


def minimum_cost_estimator(Checkpoints, Costs, Gas):
    """Returns the minimum cost to travel
       to coderland, given the checkpoints,
       gas cost and minimum gas needed """
    minimum_cost = 0
    min_petrol = sys.maxsize
    for index, cost in enumerate(Costs):
        min_petrol = min(min_petrol, cost)
        minimum_cost += min_petrol * Gas[index]
    return minimum_cost


def get_input():
    '''Gets the user input'''
    T = int(input())  # Test Cases
    for testcase in range(T):
        N = int(input())  # Checkpoints
        C = list(map(int, input().strip().split()))
        L = list(map(int, input().strip().split()))
        min_cost = minimum_cost_estimator(N, C, L)
        print(min_cost)


if __name__ == "__main__":
    get_input()
