class FreqStack:
    """
    A Maximum Frequency Stack implementation.
    Elements are popped based on maximum frequency. In case of a tie,
    the element pushed closest to the top of the stack is popped.
    """

    def __init__(self):
        # levels: A list of stacks. levels[i] stores elements that have reached frequency i + 1.
        self.levels = []
        # frequency: A map to keep track of the exact frequency count of each element.
        self.frequency = {}

    def push(self, val: int) -> None:
        """Adds an element to the stack and updates its frequency levels."""
        # Update the element's frequency count
        self.frequency[val] = self.frequency.get(val,0) + 1
        
        # If this frequency is higher than any we've seen before, create a new frequency level stack
        if len(self.levels) < self.frequency[val]:
            self.levels.append([])
            
        # Append the element to the stack corresponding to its current frequency
        self.levels[self.frequency[val] - 1].append(val)

    def pop(self) -> int:
        """Removes and returns the most frequent element. Ties broken by most recently added."""
        # Pop the most recently added element from the highest frequency level stack
        val = self.levels[-1].pop()
        
        # If the highest frequency level stack is now empty, remove that level entirely
        if len(self.levels[-1]) == 0:
            self.levels.pop()
            
        # Decrement the element's overall frequency
        self.frequency[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

def main():
    obj = FreqStack()
    obj.push(10)
    print(obj.pop())
    obj.push(20)
    print(obj.pop())
    

if __name__ == "__main__":
    main()
