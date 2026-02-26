class TimeMap:
    """
    A time-based key-value store that supports retrieving the value of a key 
    at a specific timestamp or the closest previous timestamp.
    """

    def __init__(self):
        # Dictionary to store key -> list of (timestamp, value) tuples
        self.storing = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Stores the key with the value at the given timestamp.
        Assumes timestamps are added in strictly increasing order.
        """
        temp = (timestamp, value)
        if key not in self.storing:
            self.storing[key] = [temp]
        else:
            self.storing[key].append(temp)

    def get(self, key: str, timestamp: int) -> str:
        """
        Returns the value such that set was called with the same key and 
        timestamp_prev <= timestamp. If there are multiple such values, 
        it returns the one associated with the largest timestamp_prev.
        """
        # Get the list of (timestamp, value) pairs for the given key
        # Default to an empty list if the key doesn't exist
        lol = self.storing.get(key, [])
        l, r = 0, len(lol) - 1
        stamp = None
        
        # Binary search can be used because timestamps are stored in chronological order.
        # We search for the largest timestamp that is less than or equal to the target.
        while l <= r:
            mid = (l + r) // 2
            # If current timestamp at mid is less than or equal to target
            if timestamp >= lol[mid][0]:
                stamp = lol[mid][1]  # This is a potential candidate
                l = mid + 1          # Keep searching in the right half for a possible better (larger) timestamp
            else:
                r = mid - 1          # Look for a smaller timestamp in the left half
        return stamp

def main():
    # Example usage
    timestamp = TimeMap()
    timestamp.set("foo", "bar", 1)
    print(f"Get 'foo' at 1: {timestamp.get('foo', 1)}") # Expected: "bar"
    print(f"Get 'foo' at 3: {timestamp.get('foo', 3)}") # Expected: "bar" (closest previous)
    
    timestamp.set("foo", "bar2", 4)
    print(f"Get 'foo' at 4: {timestamp.get('foo', 4)}") # Expected: "bar2"
    print(f"Get 'foo' at 5: {timestamp.get('foo', 5)}") # Expected: "bar2" (closest previous)

if __name__ == '__main__':
    main()
