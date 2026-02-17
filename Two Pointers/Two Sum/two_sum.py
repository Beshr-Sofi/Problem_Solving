def twoSum(numbers, target):
    """
    Find two numbers in a sorted array that sum to a target value.
    
    This is a custom implementation for LeetCode problem 167: Two Sum II - Input Array Is Sorted.
    It uses a two-pointer approach but with a non-standard sliding window technique.
    
    The algorithm maintains a window [l, r] and adjusts it based on the current sum:
    - If sum equals target: return indices (1-based)
    - If sum > target or r is out of bounds: shrink window from left and reset right
    - If sum < target: expand window to the right
    
    Note: This implementation is more complex than necessary and has potential bugs.
    
    Time Complexity: O(n²) in worst case due to resetting pointers
    Space Complexity: O(1)
    
    Args:
        numbers (list): Sorted array of integers
        target (int): Target sum to find
        
    Returns:
        list: 1-based indices of the two numbers that sum to target
    """
    # Initialize left and right pointers
    l, r = 0, 1
    # Calculate initial sum
    sum = numbers[l] + numbers[r]
    
    # Continue until left pointer reaches the end
    while l < len(numbers):
        # Case 1: Found the target sum
        if sum == target:
            return [l+1, r+1]  # Return 1-based indices
        
        # Case 2: Current sum is too large OR right pointer is out of bounds
        elif sum > target or r >= len(numbers):
            # Move left pointer forward and reset right pointer
            l, r = l+1, l+2
            # Recalculate sum if within bounds
            if r < len(numbers):
                sum = numbers[l] + numbers[r]
        
        # Case 3: Current sum is too small
        else:
            # Check if we're at the end of array
            if r + 1 >= len(numbers):
                r += 1
                continue
            
            # Expand window to the right
            # Remove the current right element from sum
            sum -= numbers[r]
            # Move right pointer forward
            r += 1
            # Add the new right element to sum
            sum += numbers[r]

def twoSum2(numbers, target):
    """
    Find two numbers in a sorted array that sum to a target value.
    
    This is the standard optimal solution for LeetCode problem 167: Two Sum II.
    It uses the classic two-pointer technique from both ends of the array.
    
    Algorithm:
    1. Start with left pointer at beginning, right pointer at end
    2. Calculate current sum = numbers[l] + numbers[r]
    3. If sum == target: return indices (1-based)
    4. If sum > target: need smaller sum, move right pointer left
    5. If sum < target: need larger sum, move left pointer right
    6. Repeat until pointers meet
    
    Time Complexity: O(n) - single pass through the array
    Space Complexity: O(1) - constant extra space
    
    Args:
        numbers (list): Sorted array of integers
        target (int): Target sum to find
        
    Returns:
        list: 1-based indices of the two numbers that sum to target
    """
    # Initialize left pointer at start, right pointer at end
    l, r = 0, len(numbers) - 1
    
    # Continue until pointers meet
    while l < r:
        # Calculate current sum
        sum = numbers[l] + numbers[r]
        
        # Case 1: Found the target sum
        if sum == target:
            return [l+1, r+1]  # Return 1-based indices
        
        # Case 2: Current sum is too large
        elif sum > target:
            r -= 1  # Move right pointer left to decrease sum
        
        # Case 3: Current sum is too small
        else:
            l += 1  # Move left pointer right to increase sum

def main():
    """
    Main function to demonstrate both two-sum implementations.
    
    Tests with:
    numbers = [-5, -3, 0, 2, 4, 6, 8]
    target = 5
    
    Expected output: [4, 6] because numbers[3] + numbers[5] = 2 + 6 = 8? Wait, that's 8, not 5.
    Let's find the correct pair: -3 + 8 = 5 → indices 2 and 7? But array has 7 elements, max index 6.
    Actually: 0 + 5? No 5 not in array. -5 + 10? No.
    Let's check: -3 + 8 = 5 (indices 1 and 6) but 8 is at index 6.
    Wait, numbers[1] = -3, numbers[6] = 8 → sum = 5 ✓
    So expected: [2, 7] (1-based indices)
    """
    numbers = [-5, -3, 0, 2, 4, 6, 8]
    target = 5
    
    # Test first implementation
    print(twoSum(numbers, target))
    
    # Test second (optimal) implementation
    print(twoSum2(numbers, target))

if __name__ == "__main__":
    main()
