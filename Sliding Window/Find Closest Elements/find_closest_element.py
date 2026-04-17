def findClosestElements(arr, x, k):
    """
    Finds the k closest elements to a target x in an array arr using a Sliding Window approach.
    It assumes the array is sorted, meaning the k closest elements will be contiguous.
    
    Time Complexity: O(N) where N is the length of the array, since it traverses the array once.
    Space Complexity: O(k) or O(1) depending on whether the output subarray space is counted.
    """
    sumDistance = 0
    resDistance = float('inf')
    res = []
    start = 0
    
    # Iterate through the array to form and slide our window of size k
    for i in range(len(arr)):
        # Once we've accumulated k elements (from index 0 to k-1), our window is full.
        # Now we can start comparing and sliding the window.
        if i > k - 1:
            # Check if the current window's sum of distances is smaller than the best we found
            if resDistance > sumDistance:
                res = arr[start:i] # Snapshot the elements currently in the window
                resDistance = sumDistance # Update the minimum distance
            
            # Slide the window rightward by 1 element:
            # 1. Remove the distance of the element leaving the window from the left (start index)
            sumDistance -= abs(arr[start] - x)
            # 2. Add the distance of the new element entering the window from the right (index i)
            sumDistance += abs(arr[i] - x)
            # 3. Move the window's left edge
            start += 1
        else:
            # Initial phase: just build the first window of size k by adding distances
            sumDistance += abs(arr[i] - x)
            
    # After the loop, check if the last window was better than the recorded minimum
    return res if resDistance <= sumDistance else arr[start:len(arr)]

def main():
    arr = [1, 2, 3, 4, 5]
    target = 3
    k = 4
    # Example Output: [1, 2, 3, 4] (distances to 3 are 2, 1, 0, 1 -> sum is 4)
    # The last window [2, 3, 4, 5] has distances 1, 0, 1, 2 -> sum is 4.
    # Because 4 <= 4 is true, the first subset found with that distance is returned.
    print(findClosestElements(arr, target, k))

if __name__ == "__main__":
    main()
