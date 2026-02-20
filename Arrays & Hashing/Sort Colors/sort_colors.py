def sortColors(nums):
    """
    Sort an array containing only 0, 1, and 2 in-place (Dutch National Flag problem).
    
    This is LeetCode problem 75: Sort Colors. The array contains only three distinct values:
    0 (red), 1 (white), and 2 (blue). The goal is to sort them in-place so that all 0s
    come first, then all 1s, then all 2s.
    
    This implementation uses counting sort approach:
    1. Count the frequency of each color (0, 1, 2)
    2. Overwrite the original array with the counted values in order
    
    Time Complexity: O(n) where n is the length of the array
    Space Complexity: O(1) - uses constant extra space (counter array of size 3)
    
    Args:
        nums (list): Array containing only integers 0, 1, and 2 (modified in-place)
    """
    # Step 1: Count frequencies of each color
    # Create a counter array of size 3 (for values 0, 1, and 2)
    counter = [0] * 3
    
    # Iterate through the array and count occurrences
    for i in nums:
        counter[i] += 1  # Increment count for value i (0, 1, or 2)
    
    # Step 2: Overwrite the original array with sorted values
    position = 0  # Current position to write in the original array
    
    # Iterate through each possible value (0, then 1, then 2)
    for i in range(len(counter)):
        # Write value i as many times as it appears in the original array
        while counter[i]:
            nums[position] = i      # Place the value at current position
            position += 1           # Move to next position
            counter[i] -= 1         # Decrease the count

def main():
    """
    Main function to demonstrate sorting colors (0s, 1s, and 2s).
    
    Tests the sortColors function with:
    nums = [1, 0, 1, 2]
    
    Expected output: [0, 1, 1, 2]
    """
    # Input array containing 0s, 1s, and 2s in unsorted order
    nums = [1, 0, 1, 2]
    
    # Sort the array in-place
    sortColors(nums)
    
    # Print the sorted array
    print(nums)

if __name__ == '__main__':
    main()
