class Solution:
    """
    Solves the 'Last Stone Weight' problem using a custom Max-Heap implementation.
    
    Problem:
    We have a collection of stones. Each turn, we choose the two heaviest stones and smash them together.
    If they have the same weight, both are destroyed. If they have different weights, the lighter one is destroyed,
    and the heavier one's weight is reduced by the lighter's weight. Return the weight of the last remaining stone.
    
    Approach:
    - Convert the input list into a Max-Heap in O(N) time using a bottom-up `heapifyDown` approach.
    - Repeatedly extract the two largest elements (which take O(log N) each).
    - If they differ, push their difference back into the heap taking O(log N) using `heapifyUp`.
    
    Time Complexity: O(N + K log N) where N is the number of stones and K is the number of smashes.
    Space Complexity: O(1) auxiliary space (done in-place by modifying the input array).
    """
    def lastStoneWeight(self, stones) -> int:
        for i in range(len(stones)//2,-1,-1):
            self.heapifyDown(stones, i)
        while len(stones) > 1:
            maxi1 = stones[0]
            stones[0] = stones[-1]
            stones.pop()
            self.heapifyDown(stones,0)
            
            maxi2 = stones[0]
            stones[0] = stones[-1]
            stones.pop()
            self.heapifyDown(stones,0)

            if maxi1 != maxi2:
                stones.append(maxi1 - maxi2)
                self.heapifyUp(stones)
        
        return stones[0] if len(stones) else 0

    def heapifyDown(self, nums, index):
        """
        Sinks a node down the tree to maintain the max-heap property.
        Compares the current node with its children and swaps it with the largest child
        if the child is greater than the current node. Repeats this process until the node
        is larger than both its children or it becomes a leaf.
        """
        size = len(nums)
        largest = index
        while True:
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and nums[left] > nums[largest]:
                largest = left

            if right < size and nums[right] > nums[largest]:
                largest = right

            if largest != index:
                nums[largest], nums[index] = nums[index], nums[largest]
                index = largest
            
            else: break
        
    def heapifyUp(self, nums):
        """
        Bubbles a newly added node up the tree to maintain the max-heap property.
        Compares the newly added node (at the end of the array) with its parent.
        If it is larger than its parent, they are swapped. Repeats until the root is reached
        or the node is no longer larger than its parent.
        """
        index = len(nums) - 1
        parent = (index - 1) >> 1

        while index != 0 and nums[index] > nums[parent]:
            nums[index], nums[parent] = nums[parent], nums[index]
            index = parent
            parent = (index - 1) >> 1

def main():
    stones = [2,7,4,1,8,1]
    solution = Solution()
    print(solution.lastStoneWeight(stones))

if __name__ == "__main__":
    main()


