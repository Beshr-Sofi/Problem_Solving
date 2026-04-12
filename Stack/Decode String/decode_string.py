def decodeString(s: str) -> str:
    """
    Decodes an encoded string where k[encoded_string] means the encoded_string 
    inside the square brackets is repeated exactly k times.
    Uses a Stack to elegantly resolve nested brackets from the inside out.
    """
    stack = []
    
    for i in s:
        # If the character is not a closing bracket, push it straight onto the stack.
        # This sweeps up letters, numbers, and the opening brackets '['.
        if i != ']':
            stack.append(i)
        else:
            # We found a ']', meaning we have reached the end of an encoded segment.
            # Step 1: Extract the string inside the brackets.
            tmp = ''
            while stack and stack[-1] != '[':
                tmp = stack.pop() + tmp
                
            # Step 2: Pop the literal '[' out of the stack and throw it away.
            stack.pop()
            
            # Step 3: Extract the number multiplier sitting right before the '['.
            number = ''
            # Numbers can be multiple digits (like '100[a]'), so we keep popping while there are digits.
            while stack and stack[-1].isdigit():
                number = stack.pop() + number
                
            # Step 4: Multiply the string we extracted by the number, and push it BACK onto the stack.
            # Pushing it back is essential because this string might be inside another set of larger brackets!
            stack.append(tmp * int(number))
            
    # After iterating through the whole string, the stack holds our fully decoded, flattened pieces.
    return ''.join(stack)

def main():
    s = "2[a3[b]]c"
    print(decodeString(s))

if __name__ == "__main__":
    main()
