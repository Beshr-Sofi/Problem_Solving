import heapq

class KthLargest:
    """
    Design a class to find the kth largest element in a stream.
    
    Approach: Min-Heap
    - We maintain a min-heap of size exactly `k`.
    - The min-heap stores the `k` largest elements seen so far.
    - Because it's a min-heap, the smallest of these `k` elements is always at the root (index 0).
    - Therefore, the root of the heap is always our kth largest element.
    
    Time Complexity:
    - __init__: O(N log N) where N is the length of `nums`. heapify is O(N), but we pop N-k times.
    - add: O(log k). We push and potentially pop from a heap of size k (or k+1).
    
    Space Complexity: O(N) initially to store all elements, but it gets reduced to O(k) 
    since we only keep at most `k` elements in the heap.
    """
    def __init__(self, k: int, nums):
        self.minHeap, self.k = nums, k
        
        # Transform the list into a valid min-heap in-place in O(N) time
        heapq.heapify(self.minHeap)
        
        # Keep popping the smallest elements until we are left with exactly `k` elements
        # These remaining `k` elements are the largest ones, with the smallest of them at the top
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        
    def add(self, val: int) -> int:
        # Add the new value to the heap
        heapq.heappush(self.minHeap, val)
        
        # If the heap size exceeds `k`, pop the smallest element
        # to maintain the size of the heap at `k`
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
            
        # The root of the min-heap is the kth largest element
        return self.minHeap[0]

def main():
    k = 3
    nums = [4, 5, 8, 2]
    kthLargest = KthLargest(k, nums)
    print(kthLargest.add(3))
    print(kthLargest.add(5))
    print(kthLargest.add(10))
    print(kthLargest.add(9))
    print(kthLargest.add(4))

if __name__ == "__main__":
    main()
