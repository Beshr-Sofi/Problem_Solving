def findDuplicateFloyd(nums):
    """
    Find the duplicate number in an array using Floyd's Tortoise and Hare algorithm.
    
    This implementation uses Floyd's Cycle Detection algorithm (also known as 
    Tortoise and Hare) to find the duplicate number in an array where:
    - Each integer is between 1 and n (inclusive)
    - There is exactly one duplicate number (may appear more than twice)
    - Array length is n+1 (contains n+1 integers)
    
    The key insight: Treat the array as a linked list where each element 
    points to the next index (nums[i] is the "next" node). The duplicate 
    creates a cycle in this linked list representation.
    
    Example: [1,3,4,2,2] 
    Think of it as: 0→1, 1→3, 2→4, 3→2, 4→2
    This forms a cycle: 2→4→2→4→...
    
    Time Complexity: O(n) - linear time
    Space Complexity: O(1) - constant extra space
    
    Args:
        nums (list): Array of integers with exactly one duplicate
        
    Returns:
        int: The duplicate number found in the array
    """
    # Phase 1: Detect if a cycle exists using slow and fast pointers
    # Both start at index 0 (value at nums[0] is the first "next" pointer)
    slow, fast = 0, 0
    
    while True:
        # Move slow pointer one step: slow = nums[slow]
        slow = nums[slow]
        
        # Move fast pointer two steps: fast = nums[nums[fast]]
        fast = nums[nums[fast]]
        
        # If slow and fast meet, a cycle is detected
        if slow == fast:
            break
    
    # Phase 2: Find the entrance to the cycle (which is the duplicate number)
    # Reset one pointer to start, keep other at meeting point
    # Move both one step at a time until they meet again
    slow2 = 0
    
    while True:
        # Move both pointers one step at a time
        slow = nums[slow]    # Continue from meeting point
        slow2 = nums[slow2]  # Start from beginning
        
        # When they meet, that's the entrance to the cycle (duplicate number)
        if slow == slow2:
            return slow

def main():
    """
    Main function to demonstrate Floyd's algorithm for finding duplicates.
    
    Tests the findDuplicateFloyd function with a sample array:
    [1,3,4,2,2] contains numbers 1-4 with 2 duplicated.
    
    The algorithm should return 2, which is the duplicate number.
    """
    # Test case: array of length 5 containing numbers 1-4 with one duplicate
    nums = [1,3,4,2,2]
    print(findDuplicateFloyd(nums))

if __name__ == "__main__":
    main()
