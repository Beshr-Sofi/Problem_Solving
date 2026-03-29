def carFleet(target, position, speed):
    """
    Calculates the number of car fleets that will arrive at the destination.
    A car fleet is a group of one or more cars driving at the same speed.
    Cars cannot pass each other; a faster car catching up to a slower car
    becomes part of the slower car's fleet.
    """
    # Pair each car's starting position with its speed.
    pair = [[p, s] for p, s in zip(position, speed)]
        
    stack = []
    
    # Sort the cars by starting position in descending order (closest to target first).
    # We evaluate from the front to the back because cars ahead dictate the speed of cars behind.
    for p, s in sorted(pair)[::-1]:
        # Calculate the time it takes for this car to reach the target on its own.
        # Time = (Distance remaining) / Speed
        stack.append((target - p) / s)
        
        # If there are at least 2 times recorded, verify if a collision occurs.
        # A collision happens if the car we just processed (which started further back) 
        # takes LESS OR EQUAL time to reach the target compared to the car directly ahead of it.
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            # The trailing car catches up to the car ahead and merges into its fleet.
            # It will now be forced to drive at the slower car's pace.
            # We remove its individual arrival time since it belongs to the leading fleet.
            stack.pop()
    
    # The number of surviving, distinct arrival times left in the stack is the number of fleets.
    return len(stack)

def main():
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    print(carFleet(target, position, speed))

if __name__ == "__main__":
    main()
