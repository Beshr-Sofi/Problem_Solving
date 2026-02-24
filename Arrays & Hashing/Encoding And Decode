def encode(strs):
    """
    Encodes a list of strings into a single string using semicolon delimiter.
    
    This function attempts to join strings with a semicolon separator.
    
    Args:
        strs (list): List of strings to encode
        
    Returns:
        str or None: Encoded string, or None for empty list
        
    BUG: Returns None for empty list instead of empty string
    """
    # If list is not empty, join with semicolons
    # If list is empty, return None (this is the bug)
    return ';'.join(strs) if len(strs) > 0 else None

def decode(s):
    """
    Decodes a semicolon-delimited string back into a list of strings.
    
    Args:
        s (str or None): Encoded string to decode
        
    Returns:
        list: Decoded list of strings
    """
    # Handle None input (from encode with empty list)
    if s is None:
        return []
    
    # Split on semicolon to get original strings
    tmp = s.split(';')
    return tmp

def main():
    """
    Main function to demonstrate the encoding/decoding with empty list.
    
    Creates an empty list, encodes it, then decodes the result.
    """
    # Empty input list
    s = []
    
    # Encode the empty list - this returns None
    lol = encode(s)
    print(f"Encoded result: {lol}")  # Prints: Encoded result: None
    
    # Decode the result - this handles None and returns []
    result = decode(lol)
    print(f"Decoded result: {result}")  # Prints: Decoded result: []

if __name__ == '__main__':
    main()
