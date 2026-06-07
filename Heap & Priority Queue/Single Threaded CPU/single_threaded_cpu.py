import heapq

def getOrder(tasks):
    """
    Simulate a Single-Threaded CPU executing tasks.
    Each task is given as [enqueueTime, processingTime].
    
    Rules:
    - The CPU executes the available task with the shortest processing time.
    - If there is a tie, it executes the task with the smallest original index.
    - If no tasks are available, the CPU jumps to the time of the next task.
    
    Approach: Sorting + Min-Heap
    - First, we append the original index to each task so we can return it later.
    - We sort the tasks by their enqueueTime so we can process them chronologically.
    - We maintain a `time` variable. All tasks with enqueueTime <= `time` are pushed
      into a Min-Heap. The Min-Heap stores tuples of (processingTime, originalIndex).
    - We pop from the Min-Heap to get the shortest task, add its index to our result,
      and advance `time` by its processingTime.
      
    Time Complexity: O(N log N)
    - Sorting the tasks takes O(N log N).
    - Pushing and popping N elements from the heap takes O(N log N).
    
    Space Complexity: O(N) to store the Min-Heap and the result array.
    """
    # Append the original index to keep track of it after sorting
    for i in range(len(tasks)):
        tasks[i].append(i)

    # Sort tasks primarily by enqueueTime
    tasks.sort(key=lambda x: x[0])

    res = []
    minHeap = []
    i = 0
    time = 0
    n = len(tasks)

    while i < n or minHeap:
        # If no tasks are available in the heap, jump time forward to the next task's enqueueTime
        if not minHeap and time < tasks[i][0]:
            time = tasks[i][0]
        
        # Add all tasks that have arrived up to the current `time` into the Min-Heap
        while i < n and tasks[i][0] <= time:
            # Push (processingTime, originalIndex)
            heapq.heappush(minHeap, (tasks[i][1], tasks[i][2]))   
            i += 1

        # Pop the task with the shortest processingTime (and smallest index on tie)
        process, index = heapq.heappop(minHeap)
        
        # Execute the task
        time += process
        res.append(index)
        
    return res

def main():
    tasks = [[5,2],[4,4],[4,1],[2,1],[3,3]]

    print(getOrder(tasks))

if __name__ == "__main__":
    main()
