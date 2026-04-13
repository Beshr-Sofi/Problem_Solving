"""
IDEA: Largest Rectangle in Histogram using Monotonic Stack

Problem: Given an array of bar heights in a histogram, find the area of the 
largest rectangle that can be formed within the histogram.

Approach:
1. Use a stack to keep track of bar indices in increasing order of heights
2. When we encounter a bar shorter than the one at stack top, the shorter bar
   becomes the right boundary for rectangles using the taller bar's height
3. For each popped bar, calculate the maximum rectangle area using its height
   - Height = height of the popped bar
   - Width = distance between right boundary (current index) and left boundary 
             (index of next element in stack, or -1 if stack is empty)
4. Add a sentinel 0 at the end to force processing of all remaining bars in stack

Time Complexity: O(n) - each bar is pushed and popped at most once
Space Complexity: O(n) - for the stack

Example:
For heights = [1,3,7]:
- Bar 0 (height 1): Stack = [0]
- Bar 1 (height 3): Stack = [0,1]
- Bar 2 (height 7): Stack = [0,1,2]
- Sentinel 0 triggers pop of 7: area = 7 * 1 = 7
- Pop 3: area = 3 * 2 = 6
- Pop 1: area = 1 * 3 = 3
- Maximum area = 7
"""

def LargestRectangleArea(heights):
    # Add a sentinel value 0 at the end to force processing of remaining bars
    heights.append(0)
    # Stack to store indices of histogram bars in increasing height order
    stack = []
    maxArea = 0
    
    # Iterate through all bars including the sentinel
    for i in range(len(heights)):
        # While current bar is shorter than the bar at stack top,
        # we've found the right boundary for rectangles using the top bar's height
        while stack and heights[stack[-1]] > heights[i]:
            # Get the height of the bar we're calculating area for
            curr = heights[stack[-1]]
            # Remove it from stack since we're done with it
            stack.pop()
            
            # Calculate left boundary:
            # If stack is empty, the rectangle extends to the beginning (index -1)
            # Otherwise, it extends to the index of the next bar in stack
            left = -1 if not stack else stack[-1]
            
            # Calculate width: right boundary (i) minus left boundary (left) minus 1
            # Multiply by height to get area
            curr *= (i - left - 1)
            
            # Update maximum area if current area is larger
            if curr > maxArea:
                maxArea = curr
        
        # Push current bar's index to stack (heights are in non-decreasing order in stack)
        stack.append(i)
    
    return maxArea

def main():
    # Example usage with heights [1, 3, 7]
    # The largest rectangle would be 1*3=3, 3*1=3, or 7*1=7, so maximum is 7
    heights = [1,3,7]
    print(LargestRectangleArea(heights))

if __name__ == "__main__":
    main()
