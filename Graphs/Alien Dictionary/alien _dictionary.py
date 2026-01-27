def alienOrder(words , order):
    """
    Verify if words are sorted according to alien dictionary order.
    
    Args:
        words: List of strings to verify
        order: String defining the character order in alien language
    
    Returns:
        bool: True if words are sorted according to alien order, False otherwise
    """
    # Create a mapping: character -> its position in alien order
    alien_order = {c:i for i,c in enumerate(order)}

    # Compare each consecutive pair of words
    for i in range(len(words)-1):
        w1, w2 = words[i], words[i+1]

        # Compare characters position by position
        for j in range(len(w2)):
            # If w1 is longer than w2 and all previous chars matched, 
            # then w1 should come after w2 (invalid ordering)
            if j == len(w1):
                return False
            
            # Find the first differing character
            if w1[j] != w2[j]:
                # Check if characters are in correct alien order
                if alien_order[w1[j]] > alien_order[w2[j]]:
                    return False
                # Characters are in correct order, move to next word pair
                break
    
    # All consecutive pairs are correctly ordered
    return True

def main():
    """
    Test cases demonstrating the alienOrder function
    """
    # Test Case 1: Words in correct order
    words = ["hello","leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    print(f"Test 1: {words}")
    print(f"Order: {order}")
    print(f"Result: {alienOrder(words, order)}")  # Output: True
    print("Explanation: 'h' comes before 'l' in the alien order\n")

    # Test Case 2: Words NOT in correct order
    words = ["word","world","row"]
    order = "worldabcefghijkmnpqstuvxyz"
    print(f"Test 2: {words}")
    print(f"Order: {order}")
    print(f"Result: {alienOrder(words, order)}")  # Output: False
    print("Explanation: 'world' should come before 'word' (world is prefix)\n")

    # Test Case 3: Longer word before prefix (invalid)
    words = ["apple","app"]
    order = "abcdefghijklmnopqrstuvwxyz"
    print(f"Test 3: {words}")
    print(f"Order: {order}")
    print(f"Result: {alienOrder(words, order)}")  # Output: False
    print("Explanation: 'apple' is longer and comes before 'app' (its prefix) - invalid!\n")

if __name__ == "__main__":
    main()
