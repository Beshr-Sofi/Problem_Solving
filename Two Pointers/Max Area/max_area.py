def maxArea(heights):
    """
    Finds the maximum area of a container that can be formed by two given lines.
    Uses a two-pointer approach to optimize the search from O(N^2) to O(N).
    
    Time Complexity: O(N), where N is the length of heights.
    Space Complexity: O(1), as it uses constant extra space.
    """
    # Initialize left (l) and right (r) pointers at the ends of the array
    l, r = 0, len(heights) - 1
    res = 0  # Stores the maximum area found
    
    while l < r:
        # The area is limited by the shorter line multiplied by the distance between them
        tmp = min(heights[l], heights[r]) * (r - l)
        
        # Update maximum area
        res = max(tmp, res)
        
        # Move the pointer of the shorter line inward to potentially find a taller line
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
            
    return res

def main():
    heights = [1,8,6,2,5,4,8,3,7]
    print(maxArea(heights))

if __name__ == "__main__":
    main()
