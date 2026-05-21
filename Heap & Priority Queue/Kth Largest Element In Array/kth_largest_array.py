import heapq

def kthLargest(nums, k):
    """
    Find the kth largest element in an array.
    
    Approach: Simulated Max-Heap
    - Python's `heapq` only provides a Min-Heap. To simulate a Max-Heap, we can 
      negate all the numbers in the array.
    - After heapifying the negated array, the largest absolute values (most negative) 
      will be at the top of the heap.
    - We pop the top element `k - 1` times to discard the (k-1) largest elements.
    - The element at the top is now the kth largest. We pop it, negate it back to 
      its original positive/negative value, and return it.
      
    Time Complexity: O(N + K log N) where N is the length of `nums`.
    - Negating the array: O(N)
    - Heapifying: O(N)
    - Popping k elements: O(K log N)
    
    Space Complexity: O(N) to store the new array with negated values.
    """
    # Create a new array with negated values to simulate a Max-Heap
    nums = [-i for i in nums]
    
    # Transform the list into a min-heap in O(N) time
    heapq.heapify(nums)
    
    # Pop the largest elements k-1 times
    for _ in range(k - 1):
        heapq.heappop(nums)
        
    # The kth largest element is now at the top of the heap.
    # Pop it and negate it to restore its original value.
    return -heapq.heappop(nums)


def main():
    nums = [3,2,1,5,6,4]
    k = 2
    print(kthLargest(nums, k))

if __name__ == "__main__":
    main()
