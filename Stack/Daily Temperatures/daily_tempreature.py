def dailyTemperatures(temperatures):
    """
    Given an array of temperatures, returns an array such that res[i] is the number 
    of days you have to wait after the i-th day to get a warmer temperature.
    If there is no future day for which this is possible, res[i] == 0.
    
    Uses a 'Decreasing Monotonic Stack' to achieve an optimal O(n) time complexity.
    """
    # Initialize the result array with 0s. 
    res = [0] * len(temperatures)
    
    # The stack will store INCIDES of the temperatures, not the temperatures themselves.
    stack = []
    
    for i in range(len(temperatures)):
        # Base case: if stack is empty, there's nothing to compare against.
        # Just push the current day's index and continue.
        if not stack:
            stack.append(i)
            continue
        
        # While the stack is not empty AND the current day's temperature is WARMER 
        # than the temperature on the day at the top of the stack...
        while stack and temperatures[i] > temperatures[stack[-1]]:
            # We found a warmer day for the day at the top of the stack!
            # The wait time is the difference between the current index (i) 
            # and the index at the top of the stack.
            res[stack[-1]] = i - stack[-1]
            
            # Remove that day from the stack because we've found its result.
            stack.pop()
        
        # Finally, push the current day's index onto the stack so we can find 
        # a warmer day for it in the future.
        stack.append(i)
        
    return res

def main():
    temperatures = [73,74,75,71,69,72,76,73]
    print(dailyTemperatures(temperatures))

if __name__ == "__main__":
    main()
