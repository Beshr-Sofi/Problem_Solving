def coinChange(coins, amount):
    """
    Find the fewest number of coins that you need to make up that amount.
    
    Approach: Top-Down Dynamic Programming (Memoization) / Unbounded Knapsack
    - We use a recursive function `helper(index, summation)` that returns the minimum 
      coins needed to reach `amount` starting from the current `summation` and considering 
      coins from `index` onwards.
    - Base case 1: If `summation == amount`, we need 0 more coins.
    - Base case 2: If we exceed the `amount` or run out of coins to check, it's impossible, 
      so we return infinity.
    - Recursive step: At each step, we have two choices:
        1. Include the coin at `index` (add its value to `summation` and add 1 to our coin count).
           Since we have an infinite number of each coin, we stay at the same `index`.
        2. Skip the coin at `index` and move to `index + 1` (summation stays the same).
    - We take the minimum of these two choices and cache it in `dp[(index, summation)]`.
      
    Time Complexity: O(N * A) where N is the number of coins and A is the `amount`. 
      There are N * A unique states we can visit, and each takes O(1) time.
    Space Complexity: O(N * A) for the recursion stack and the `dp` dictionary.
    """
    dp = {}
    def helper(index, summation):
        # Base case: successfully reached the exact amount
        if summation == amount:
            return 0

        # Base case: exceeded amount or ran out of coin types
        if summation > amount or index == len(coins):
            return float('inf')

        # Return cached result if already computed
        if (index, summation) in dp:
            return dp[(index, summation)]
        
        # Two choices: take the coin (stay at same index) OR skip the coin (move to next index)
        dp[(index, summation)] = min(helper(index, summation + coins[index]) + 1,
                            helper(index + 1, summation))
        return dp[(index, summation)]

    result = helper(0,0)
    # If result is infinity, it means it's impossible to make the amount
    return result if result != float('inf') else -1

def main():
    coins = [1, 2, 5]
    amount = 11
    print(coinChange(coins, amount))

if __name__ == "__main__":
    main()
