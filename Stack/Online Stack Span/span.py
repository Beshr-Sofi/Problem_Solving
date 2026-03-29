class StockSpanner:
    """
    Computes the 'span' of a stock's price for the current day.
    The span is the maximum number of consecutive days (starting from today and going backward)
    for which the stock price was less than or equal to today's price.
    
    Uses a 'Decreasing Monotonic Stack' for an optimal O(1) amortized time complexity per call.
    """
    def __init__(self):
        # The stack will store tuples in the format: (price, span_for_that_price)
        self.stack = []

    def next(self, price: int) -> int:
        """
        Processes a new daily price and returns its calculated span.
        """
        # The minimum span for any given day is 1 (representing the day itself).
        span = 1
        
        # While the stack is not empty AND the current price is greater than or equal to 
        # the price at the top of the stack...
        while self.stack and price >= self.stack[-1][0]:
            # The current price "absorbs" the span of the previous smaller/equal price.
            # We add its span to our current total span.
            span += self.stack[-1][1]
            
            # Since the previous price is smaller than or equal to the current price, 
            # it will never be the stopping point for any future prices. 
            # We can safely discard it from the stack!
            self.stack.pop()
            
        # Push the current price and its accumulated total span onto the stack 
        # so future days can compare against it.
        self.stack.append((price, span))
        
        return span
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

def main():
    stockSpanner = StockSpanner()
    print(stockSpanner.next(100))
    print(stockSpanner.next(80))
    print(stockSpanner.next(60))
    print(stockSpanner.next(70))
    print(stockSpanner.next(60))
    print(stockSpanner.next(75))
    print(stockSpanner.next(85))

if __name__ == "__main__":
    main()
