from collections import defaultdict
def checkInclusion(s1,s2):
    """
    Checks if s2 contains a permutation of s1.
    Uses a Sliding Window approach to keep track of character frequencies.
    Time Complexity: O(len(s1) + len(s2)), as we traverse strings linearly.
    Space Complexity: O(1), since dictionaries hold at most 26 lowercase English letters.
    """
    check = defaultdict(int)
    check2 = defaultdict(int)
    
    # Count frequencies of characters for s1, and for the initial sliding window of size len(s1) in s2
    for i in range(len(s1)):
        check[s1[i]] += 1
        if i < len(s2):
            check2[s2[i]] += 1
    
    # Slide the window of size len(s1) across the rest of s2
    for i in range(len(s1),len(s2)):
        # If the character frequencies match exactly, we've found our permutation
        if check == check2:
            return True
        
        # Include the new character entering the window from the right
        check2[s2[i]] += 1
        
        # Discard the character that is falling out of the window's left edge
        check2[s2[i - len(s1)]] -= 1
        
        # Crucial step: Remove the key entirely from the hash map if its count hits 0
        # Otherwise, dictionary comparison `check == check2` will fail
        if check2[s2[i - len(s1)]] == 0:
            del check2[s2[i - len(s1)]]
            
    # One last check to see if the string ended on a match
    return check == check2

def main():
    s1 = 'adc'
    s2 = 'dcda'
    print(checkInclusion(s1,s2))

if __name__ == "__main__":
    main()

    

