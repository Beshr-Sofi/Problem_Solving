def maxProfit(prices):
    """
    Calculates the maximum profit from buying and selling a stock multiple times.
    This approach simulates finding a local minimum to 'buy' and the next local maximum to 'sell'.
    """
    taked = prices[0] # The price at which we currently "hold" the stock
    profit = 0
    i = 1
    while i < len(prices):
        if prices[i] < taked:
            # If the price drops, we update our buy price to the lower value
            taked = prices[i]
        else:
            j = i + 1
            # Continue to the next days as long as the price keeps increasing (finding the peak)
            while j < len(prices) and prices[j] > prices[j-1]:
                j += 1
            # Sell at the peak to capture the profit
            profit += prices[j-1] - taked
            if not j < len(prices):
                return profit # If we've reached the end of the array, return the accumulated profit
            
            # Update the index to the day after the peak and buy at the new price
            i = j
            taked = prices[i]
        i += 1
    return profit

def maxProfit2(prices):
    """
    Calculates the maximum profit using an optimal greedy approach.
    Instead of finding explicit local minimums and maximums, it simply captures the profit
    from every consecutive day where the price increases.
    """
    profit = 0
    for i in range(1, len(prices)):
        # If today's price is higher than yesterday's, we "buy" yesterday and "sell" today
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit

def main():
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))
    print(maxProfit2(prices))

if __name__ == '__main__':
    main()
