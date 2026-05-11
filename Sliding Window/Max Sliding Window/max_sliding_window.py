from collections import deque

def maxSlidingWindow(nums, k):
    """
    Finds the maximum value in every sliding window of size 'k'.
    
    Approach 1: Naive (Brute Force)
    -------------------------------
    Maintains a deque of exactly size 'k' containing the actual numbers.
    Every time the window slides, it uses Python's built-in `max()` function 
    to scan the entire deque and find the largest number.
    
    Time Complexity: O(N * k) - Calling max() takes O(k) time, and we do this 
                     for almost every element. If k is large, this will cause 
                     a Time Limit Exceeded (TLE) error.
    Space Complexity: O(k) - The deque stores k elements.
    """
    deq = deque()
    res = []
    
    for i in range(len(nums)):
        # Fill the first window
        if i < k:
            deq.append(nums[i])
        # Slide the window
        else:
            res.append(max(deq))   # Very slow!
            deq.popleft()          # Remove oldest element
            deq.append(nums[i])    # Add newest element

    # Append the max of the final window
    res.append(max(deq))
    return res

def maxSlidingWindow2(nums, k):
    """
    Approach 2: Monotonically Decreasing Deque (Optimized)
    ------------------------------------------------------
    This is an elegant O(N) solution. Instead of checking every number, we use 
    a specialized deque that ONLY stores "useful" numbers.
    
    The Core Idea:
    If a new number enters the window, any smaller numbers that came BEFORE it 
    are completely useless! They can never be the maximum because the new, larger 
    number will outlive them in the sliding window. 
    By constantly popping these useless numbers, our deque naturally sorts itself 
    so the LARGEST number is always sitting right at the front!
    
    Algorithm:
    We store INDICES in the deque (not values) so we can easily check if an 
    element has fallen out of the left side of our window.
    
    1. Maintain Monotonicity: Before adding `nums[r]`, pop elements from the 
       BACK of the deque if they are smaller than `nums[r]`.
    2. Add to Deque: Append the index `r` to the back.
    3. Remove Out-of-Bounds: Check if the index at the FRONT of the deque (`q[0]`) 
       has fallen behind our left boundary `l`. If so, pop it from the front.
    4. Record Result: Once our window has expanded to size `k` (`r + 1 >= k`), 
       the absolute maximum of the window is guaranteed to be at the front!
       We add it to our output and slide the left boundary `l` forward.
       
    Time Complexity: O(N) - Every index is pushed and popped at most once.
    Space Complexity: O(k) - The deque stores at most k indices.
    """
    output = []
    q = deque()  # Stores INDICES, not values!
    l = r = 0

    while r < len(nums):
        # 1. Pop smaller useless numbers from the back
        while q and nums[q[-1]] < nums[r]:
            q.pop()
            
        # 2. Add the current index
        q.append(r)

        # 3. If the largest number (at the front) is no longer in our window, pop it
        if l > q[0]:
            q.popleft()

        # 4. Once the window is fully sized (k), start recording results
        if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1 # Slide the left side of the window
            
        r += 1 # Slide the right side of the window

    return output

def main():
    """
    Example demonstrating Sliding Window Maximum.
    
    Window Size (k) = 3
    [1, 3, 1], 2, 0, 5 -> Max: 3
    1, [3, 1, 2], 0, 5 -> Max: 3
    1, 3, [1, 2, 0], 5 -> Max: 2
    1, 3, 1, [2, 0, 5] -> Max: 5
    """
    nums = [1, 3, 1, 2, 0, 5]
    k = 3
    
    print("Approach 1 (Naive):     ", maxSlidingWindow(nums, k))
    print("Approach 2 (Monotonic): ", maxSlidingWindow2(nums, k))

if __name__ == "__main__":
    main()
