def numRescueBoats(people, limit):
    """
    Calculates the minimum number of boats required to carry all people.
    Each boat can carry at most 2 people at the same time, provided their combined weight 
    is at most the given limit.
    
    Uses a greedy two-pointer approach after sorting the array.
    
    Time Complexity: O(N log N), where N is the length of people array (due to sorting).
    Space Complexity: O(N) or O(1) depending on the sorting algorithm implementation.
    """
    # Sort the array so we can easily pair the lightest and heaviest people
    people.sort()
    
    # Initialize pointers at the lightest (left) and heaviest (right) person
    l, r = 0, len(people) - 1
    res = 0  # To keep track of the number of boats used
    
    while l <= r:
        # If the heaviest person and the lightest person together exceed the weight limit,
        # the heaviest person must go in a boat alone.
        if people[l] + people[r] > limit:
            r -= 1
        # If they can both fit within the limit, pair them up in one boat.
        else:
            l += 1
            r -= 1
        
        # In either case, one boat is used.
        res += 1
        
    return res

def main():
    people = [1,2,3,4,5,6,7,8,9,10]
    limit = 10
    print(numRescueBoats(people, limit))

if __name__ == "__main__":
    main()
