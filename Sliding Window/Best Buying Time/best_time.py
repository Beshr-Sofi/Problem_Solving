def maxProfit(prices):
    """
    Finds the maximum profit possible from buying and selling a stock once.
    
    This implementation uses a Two-Pointer (Sliding Window) approach:
    - 'buyDay' tracks the day we buy.
    - 'sellDay' tracks the day we sell.
    
    As long as selling is profitable (or even), meaning prices[sellDay] >= prices[buyDay], 
    we expand our window to the right (sellDay += 1) to see if we can get even more profit.
    The moment we find a price lower than our 'buyDay' price, we increment 'buyDay' 
    to catch up, effectively shifting our search to this new lower buy price.
    
    Time Complexity: O(N) where N is the number of days. In the worst case, both pointers 
                     traverse the array, taking at most 2N steps total.
    Space Complexity: O(1) as we only use constant extra memory.
    """
    maxProfit = float('-inf')
    buyDay = 0
    sellDay = 0
    
    while buyDay < len(prices):
        # 1. Update maxProfit with the difference of the current window
        maxProfit = max(maxProfit, prices[sellDay] - prices[buyDay])
        
        # 2. If we haven't reached the end, and the price at sellDay is GREATER OR EQUAL 
        #    to the price at buyDay, our current buyDay is good! Let's advance sellDay to 
        #    see if the next day offers an even higher profit.
        if sellDay < len(prices) - 1 and prices[sellDay] >= prices[buyDay]:
            sellDay += 1
            
        # 3. Otherwise (sell price dipped BELOW buy price, OR we reached the end of the array),
        #    it means we found a better (lower) price to buy at. We increment buyDay. 
        #    (It will incrementally catch up to the new lower price at sellDay).
        else:
            buyDay += 1
            
    return maxProfit

def main():
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))

if __name__ == "__main__":
    main()
