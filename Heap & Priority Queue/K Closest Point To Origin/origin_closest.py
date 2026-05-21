import heapq

def kthClosestOrigin(points, k):
    """
    Find the k closest points to the origin (0, 0).
    
    Approach: Min-Heap
    - We calculate the squared Euclidean distance (x^2 + y^2) for each point. We don't need
      to compute the square root because the relative order of distances remains the same.
    - We pair each distance with its corresponding point in a tuple and store them in a list.
    - We transform this list into a min-heap in O(N) time.
    - We pop the smallest elements from the min-heap `k` times to get the k closest points.
    
    Time Complexity: O(N + K log N) where N is the total number of points.
    - Creating the list of distances: O(N)
    - Heapifying the list: O(N)
    - Popping k elements: O(K log N)
    
    Space Complexity: O(N) to store the list of distances and points.
    """
    # Create a list of tuples: (squared_distance, point)
    distances = [(i[0]**2 + i[1]**2 , i) for i in points]
    
    # Transform the list into a min-heap in-place
    heapq.heapify(distances)
    
    res = []
    # Extract the smallest distance `k` times
    for _ in range(k):
        distance, point = heapq.heappop(distances)
        res.append(point)
        
    return res


def main():
    points = [[1,3],[-2,2]]
    k = 1
    print(kthClosestOrigin(points, k))

if __name__ == "__main__":
    main()
