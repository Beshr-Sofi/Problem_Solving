from collections import Counter
import heapq
from collections import deque

def taskScheduler(tasks, n):
  """
  Calculates the minimum time needed to execute all tasks with a cooldown period `n`.
  
  Approach: Max-Heap + Queue (Simulation)
  - We always want to schedule the most frequent tasks first to avoid leaving them until the end,
    which would force the CPU to sit idle due to the cooldown.
  - We use a Max-Heap to keep track of the remaining counts of the tasks available to run.
  - When a task is executed, its count is decremented. If tasks of this type remain, we cannot
    run it again for `n` intervals, so we put it in a `queue` along with its "available time".
  - At each time step, we check if the task at the front of the queue is ready to run again.
    If so, we pop it from the queue and push it back into the heap.
    
  Time Complexity: O(M) where M is the total time (idle time + number of tasks). Alternatively, 
  it can be seen as O(T log 26) = O(T) where T is the number of tasks, since the heap size is 
  bounded by 26 (uppercase English letters).
  Space Complexity: O(26) = O(1) as the dictionary, heap, and queue will store at most 26 elements.
  """
  # Count the frequencies of each task
  dic = Counter(tasks)
        
  # Simulate a Max-Heap using negative values in Python's Min-Heap
  heap = [-i for i in dic.values()]
  heapq.heapify(heap)
  
  time = 0
  queue = deque() # Stores pairs of [-count, available_time]
  
  while heap or queue:
      time += 1

      if heap:
          # Pop the most frequent task. We add 1 because it's negative (e.g., -3 + 1 = -2)
          cnt = 1 + heapq.heappop(heap)
          
          # If there are still instances of this task left to run,
          # put it in the cooldown queue to be available at `time + n`
          if cnt != 0:
              queue.append((cnt, time + n))
      
      # If the task at the front of the queue has finished its cooldown,
      # push it back into the max-heap
      if queue and queue[0][1] == time:
          heapq.heappush(heap, queue.popleft()[0])
  
  return time

def main():
  tasks = ["A", "A", "A", "B", "B", "B"]
  n = 2
  print(taskScheduler(tasks, n))

if __name__ == "__main__":
  main()
    
