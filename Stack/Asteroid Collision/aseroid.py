def asteroidCollision(asteroids):
    """
    Simulates collisions of asteroids in a straight row.
    For each asteroid, its absolute value represents its size, and its sign represents its direction
    (positive = moving right, negative = moving left).
    Returns the state of the asteroids after all collisions have resolved.
    """
    stack = []
    
    for i in asteroids:
        # A collision occurs ONLY IF there is an asteroid moving right in the stack (stack[-1] > 0)
        # and it encounters an incoming asteroid moving left (i < 0).
        while stack and stack[-1] > 0 and i < 0:
            
            # Scenario 1: The right-moving asteroid in the stack is smaller.
            if stack[-1] < -i:
                # The right-moving asteroid explodes.
                stack.pop() 
                # The while loop continues because the left-moving `i` asteroid might still hit the next right-moving asteroid in the stack.
            
            # Scenario 2: The right-moving asteroid in the stack is larger.
            elif stack[-1] > -i:
                # The incoming left-moving asteroid explodes.
                i = 0 
                # This inherently breaks the while loop condition because `i` is no longer < 0.
            
            # Scenario 3: Both asteroids are exactly the same size.
            else:
                # Both asteroids explode together.
                i = 0         # The incoming asteroid is destroyed.
                stack.pop()   # The right-moving asteroid in the stack is destroyed.
                # This also breaks the while loop condition.
                
        # If the incoming asteroid has not exploded (and thus wasn't set to 0),
        # add it to the stable configuration in the stack.
        # This includes positive numbers (moving right) and stable negative numbers.
        if i:
            stack.append(i)
            
    return stack

def main():
    asteroids = [5,10,-5]
    print(asteroidCollision(asteroids))

if __name__ == "__main__":
    main()
  
