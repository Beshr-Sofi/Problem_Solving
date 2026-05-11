from collections import defaultdict

def minWindow(s, t):
    """
    Finds the minimum window substring in 's' which contains all the characters in 't'.
    
    Approach: Sliding Window with Two Hash Maps
    -------------------------------------------
    This is the quintessential "Sliding Window" problem. We maintain a dynamic window 
    using two pointers (`start` and `end`) that stretches and shrinks as it moves 
    through the string.
    
    Data Structures:
    - `t_dic`: A reference dictionary that stores the exact frequencies of characters 
               we NEED from `t`.
    - `tmp_dic`: A dynamic dictionary tracking the frequencies of characters currently 
                 INSIDE our sliding window.
                 
    The "Have vs Need" Trick:
    Instead of comparing the two entire dictionaries on every loop (which is slow), 
    we use two integer counters:
    - `need`: The number of UNIQUE characters in `t`.
    - `have`: The number of unique characters in our current window that have 
              reached or exceeded their required frequency.
              
    Algorithm:
    1. EXPAND: Move the `end` pointer to the right. Add the new character to `tmp_dic`.
       If its frequency now matches the requirement in `t_dic`, we increment `have`.
    2. SHRINK: As soon as our window is valid (`have == need`), we want to make it 
       as small as possible. We enter a `while` loop:
       - Record the window size if it's the smallest we've seen so far.
       - Pop the left character (`s[start]`) out of the window.
       - If popping this character causes its frequency to drop BELOW our requirement, 
         we decrement `have`. This breaks the `while` loop, and we go back to Expanding!
         
    Time Complexity: O(N + M) - Where N is len(s) and M is len(t). Both pointers 
                     only ever move forward, so we visit each character at most twice.
    Space Complexity: O(1) - The dictionaries store at most 52 unique English letters.
    """
    if len(s) < len(t):
        return ""
    
    # Track the exact character counts we need from 't'
    t_dic = defaultdict(int)
    for char in t:
        t_dic[char] += 1
        
    tmp_dic = defaultdict(int)
    start = 0
    have = 0
    need = len(t_dic) # Total unique characters needed
    
    # Track the best window: [start_index, end_index] and its length
    res = [-1, -1]
    res_len = float('inf')
    
    # Standard sliding window: expand the 'end' pointer
    for end in range(len(s)):
        char = s[end]
        if char in t_dic:
            tmp_dic[char] += 1
            # Once we perfectly match the required count for this specific character
            if tmp_dic[char] == t_dic[char]:
                have += 1
                
        # Shrink the window from the 'start' pointer while the window is completely VALID
        while have == need:
            # 1. Update our minimum result if this current window is smaller
            window_size = end - start + 1
            if window_size < res_len:
                res_len = window_size
                res = [start, end]
            
            # 2. Pop the left character from the window to try and shrink it
            left_char = s[start]
            if left_char in t_dic:
                tmp_dic[left_char] -= 1
                # Only decrement 'have' if we drop BELOW the strictly required amount
                if tmp_dic[left_char] < t_dic[left_char]:
                    have -= 1
            
            start += 1
            
    # Return the sliced string if we found a valid window, otherwise return ""
    l, r = res
    return s[l:r+1] if res_len != float('inf') else ""

def main():
    """
    Example demonstrating Minimum Window Substring.
    
    s = "ADOBECODEBANC"
    t = "ABC"
    
    The algorithm will find "ADOBEC", then shrink/expand until it finds 
    the smaller "BANC" at the very end!
    """
    s = "ADOBECODEBANC"
    t = "ABC"
    print(minWindow(s, t)) # Expected Output: "BANC"

if __name__ == "__main__":
    main()
