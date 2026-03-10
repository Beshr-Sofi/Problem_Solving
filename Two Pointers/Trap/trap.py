def trap(height):
    """
    Calculates the maximum amount of trapped rain water.
    Uses an optimal two-pointer approach with O(n) time and O(1) space complexity.
    """
    if not height:
        return 0
    
    # Initialize left and right pointers at the ends of the array
    l, r = 0, len(height) - 1
    # Track the maximum heights seen so far from both sides
    maxleft, maxright = height[l], height[r]
    res = 0  # Total trapped water
    
    while l < r:
        # The water trapped at the current position depends on the smaller of the two maximums.
        if maxleft < maxright:
            l += 1  # Move left pointer forward
            maxleft = max(maxleft, height[l])  # Update maxleft if current height is taller
            res += maxleft - height[l]  # Add trapped water (if any) at current position
        else:
            r -= 1  # Move right pointer backward
            maxright = max(maxright, height[r])  # Update maxright if current height is taller
            res += maxright - height[r]  # Add trapped water (if any) at current position
            
    return res

def main():
    height = [0,2,0,3,1,0,1,3,2,1]
    print(trap(height))

if __name__ == "__main__":
    main()
