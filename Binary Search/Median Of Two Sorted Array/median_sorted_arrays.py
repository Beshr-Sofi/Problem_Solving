def findMedianSortedArrays(nums1, nums2):
    """
    Finds the median of two sorted arrays in O(log(min(m, n))) time.
    
    Approach: Binary Search on the Smaller Array
    --------------------------------------------
    Instead of merging the two arrays (which would take O(m+n) time), we can 
    find the median by finding the perfect "partition" that splits the combined 
    arrays exactly in half.
    
    The Core Idea:
    If we can cut `nums1` into a left and right half, and `nums2` into a left 
    and right half, such that:
    1. The total number of elements on the left side equals the total number of 
       elements on the right side.
    2. EVERY element on the left side is smaller than or equal to EVERY element 
       on the right side.
    Then we have successfully found the median!
    
    Algorithm:
    1. Set `A` to be the smaller array. We only run binary search on the smaller 
       array to guarantee O(log(min(m,n))) time.
    2. We guess a partition index `i` for array `A` (using binary search `l, r`).
    3. Because the left halves of `A` and `B` must perfectly add up to half of 
       the total elements, the partition index `j` for array `B` is automatically 
       forced: `j = half - i - 2`.
    4. We extract the 4 values right next to the partition cuts:
       - `Aleft`: Last element in A's left half
       - `Aright`: First element in A's right half
       - `Bleft`: Last element in B's left half
       - `Bright`: First element in B's right half
       (If a half is empty, we use infinity / negative infinity to avoid out-of-bounds).
    5. Check if the partition is perfect:
       - Is `Aleft <= Bright` AND `Bleft <= Aright`? 
         If YES, we found the perfect cut! 
         - If total length is ODD, the median is `min(Aright, Bright)`.
         - If total length is EVEN, the median is the average of the biggest 
           number on the left and the smallest number on the right.
    6. If the partition is bad:
       - If `Aleft > Bright`: `A`'s left side is too big. We move our binary 
         search to the left (`r = i - 1`).
       - Otherwise: `A`'s left side is too small. Move to the right (`l = i + 1`).
    """
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    # We always want A to be the smaller array for efficiency
    if len(B) < len(A):
        A, B = B, A

    l, r = 0, len(A) - 1
    
    while True:
        # i is the partition index for A
        i = (l + r) >> 1
        # j is the forced partition index for B
        j = half - i - 2

        # Get the edge values (default to infinity if out of bounds)
        Aleft = A[i] if i >= 0 else float('-inf')
        Aright = A[i + 1] if i + 1 < len(A) else float('inf')
        Bleft = B[j] if j >= 0 else float('-inf')
        Bright = B[j + 1] if j + 1 < len(B) else float('inf')

        # Check if the partition is perfectly valid
        if Aleft <= Bright and Bleft <= Aright:
            
            # If the total number of elements is odd
            if total & 1:
                return min(Aright, Bright)
                
            # If the total number of elements is even
            return (min(Aright, Bright) + max(Bleft, Aleft)) / 2
            
        # A's left side is too big, move search to the left
        elif Aleft > Bright:
            r = i - 1
            
        # A's left side is too small, move search to the right
        else:
            l = i + 1

def main():
    """
    Example demonstrating Median of Two Sorted Arrays.
    nums1 = [1, 3]
    nums2 = [2]
    Combined sorted array = [1, 2, 3]. Median is 2.
    """
    nums1 = [1, 3]
    nums2 = [2]
    print(findMedianSortedArrays(nums1, nums2))

if __name__ == "__main__":
    main()
