def topKFrequent(nums, k):
    """
    Find the k most frequent elements in an array using dictionary + sorting.
    
    This is LeetCode problem 347: Top K Frequent Elements.
    This implementation uses a dictionary to count frequencies, then sorts by frequency.
    
    Algorithm:
    1. Count frequencies of each element using a dictionary
    2. Sort the dictionary items by frequency (value) in descending order
    3. Return the first k keys from the sorted dictionary
    
    Time Complexity: O(n + m log m) where n is array length, m is unique elements
    Space Complexity: O(m) for storing counts
    
    Args:
        nums (list): Array of integers
        k (int): Number of top frequent elements to return
        
    Returns:
        list: The k most frequent elements (order not guaranteed)
    """
    # Step 1: Count frequencies using dictionary
    # count.get(i, 0) returns current count or 0 if key doesn't exist
    counter = {}
    for i in nums:
        counter[i] = counter.get(i, 0) + 1
    
    # Step 2: Sort dictionary items by value (frequency) in descending order
    # key=lambda item: item[1] tells sorted() to sort by the value (second element)
    # reverse=True gives highest frequencies first
    sorted_by_value = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
    
    # Step 3: Return the first k keys (most frequent elements)
    return list(sorted_by_value.keys())[:k]

def topKFrequent2(nums, k):
    """
    Find the k most frequent elements using bucket sort (optimal solution).
    
    This is the optimal approach for LeetCode 347 that achieves O(n) time complexity.
    It uses the fact that frequency cannot exceed array length to create frequency buckets.
    
    Algorithm:
    1. Count frequencies using a dictionary (O(n))
    2. Create buckets where index = frequency, value = list of elements with that frequency
    3. Traverse buckets from highest to lowest frequency and collect k elements
    
    Time Complexity: O(n) - linear time (optimal)
    Space Complexity: O(n) for buckets array
    
    Args:
        nums (list): Array of integers
        k (int): Number of top frequent elements to return
        
    Returns:
        list: The k most frequent elements (order not guaranteed)
    """
    # Step 1: Count frequencies using a dictionary
    count = {}
    for i in nums:
        count[i] = count.get(i, 0) + 1
    
    # Step 2: Create frequency buckets
    # Create a list of empty lists, size = len(nums) + 1
    # Index represents frequency, value is list of elements with that frequency
    freq = [[] for i in range(len(nums) + 1)]
    
    # Place each number in the bucket corresponding to its frequency
    for i, j in count.items():  # i = number, j = frequency
        freq[j].append(i)
    
    # Step 3: Collect results from highest frequency buckets
    res = []
    # Traverse buckets from highest frequency to lowest
    # Start from len(freq)-1 (max possible frequency) down to 1
    for i in range(len(freq) - 1, 0, -1):
        # For each element in this frequency bucket
        for j in freq[i]:
            res.append(j)
            # Once we have k elements, return immediately
            if len(res) == k:
                return res

def main():
    """
    Main function to demonstrate both top k frequent elements implementations.
    
    Tests with:
    nums = [1, 2, 2, 3, 3, 3]
    k = 2
    
    Frequency count:
    - 1 appears 1 time
    - 2 appears 2 times
    - 3 appears 3 times
    
    The 2 most frequent elements are 3 (freq=3) and 2 (freq=2)
    Expected output: [3, 2] (order may vary)
    """
    k = 2
    nums = [1, 2, 2, 3, 3, 3]
    
    # Test first implementation (dictionary + sort)
    print(topKFrequent(nums, k))
    
    # Test second implementation (bucket sort)
    print(topKFrequent2(nums, k))

if __name__ == '__main__':
    main()
