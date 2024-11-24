"""This module contains exercises of dynamic programming

    Dynamic Programming is a method for solving problems
    that can be divided into smaller sub-problems with 
    overlapping solutions and storing them to avoid recomputing them for 
    the optimal substructure.

    Making algorithm more efficient by storing some intermediate results.

    Recursion is a programming technique and can be used as a part of
    dynamic programming. 

    Recursive Time Complexity: O(2^n)
    Dynamic Programming Time Complexity: O(n) ( as storing intermediate result )
    the example case of fibonacci

    Types:
        1. Memoization: Top-down approach 
        2. Tabulation: Bottom-up approach (start solving smaller to bigger problems)
            (most effective approach)
"""
from dataset import coins_list

def fibo_memo(n: int, memo: dict = None) -> int:
    """calulates the nth fibonacci number

    Args:
        n (int): the index of fibonacci number to be calculated
        memo (dict): a dictionary to store the intermediate results

    Returns:
        int: the nth fibonacci number
    """
    if n < 0:
        raise ValueError("n cannot be negative")

    memo = memo or {}
    if n in memo:
        return memo[n]
    if n in (0, 1):
        result = n
    else:
        result = fibo_memo(n - 1, memo) + fibo_memo(n - 2, memo)
    memo[n] = result
    return result

def fib_tabulation(n: int) -> int:
    """calulates the nth fibonacci number

    Args:
        n (int): the index of fibonacci number to be calculated

    Returns:
        int: the nth fibonacci number
    """
    memo = [0] * (n + 1)
    memo[0] = 0
    memo[1] = 1
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]

def min_coins(coins: list[int], amount: int) -> int:
    """function to calculate the minimum number of coins for the given amount

    Args:
        coins (list[int]): a list of coins
        amount (int): the amount to make

    Returns:
        int: the minimum number of coins or -1 if not possible
    """
    dp = [float("inf")] * (amount + 1) #we need the amount + 1 to account for the 0th index
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if(coin - i) >= 0:
                next_dp = 1 + dp[i - coin]
                dp[i] = min(dp[i], next_dp)
    return dp[amount] if dp[amount] != float("inf") else -1

def longest_common_subsequence(s1: str, s2: str) -> int:
    """function to calculate the length of the longest common subsequence

    Args:
        s1 (str): first string
        s2 (str): second string

    Returns:
        int: length of the longest common subsequence
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

def knapsack(weights: list[int], values: list[int], capacity: int) -> int:
    """function to calculate the maximum value that can be put in a knapsack

    Args:
        weights (list[int]): a list of weights
        values (list[int]): a list of values
        capacity (int): the capacity of the knapsack

    Returns:
        int: the maximum value that can be put in the knapsack
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][capacity]
    

def main():
    """The main function to be executed"""
    print("5th fibonacci number", fibo_memo(5))
    print("5th fibonacci number using tabulation", fib_tabulation(5))
    print("Minimum number of coins to make 10", min_coins(coins_list, 11))
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    capacity = 7
    print("the knapsack problem", knapsack(weights, values, capacity))


if __name__ == "__main__":
    main()
