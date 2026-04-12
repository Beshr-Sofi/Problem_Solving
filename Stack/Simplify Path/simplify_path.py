def simplifyPath(path: str) -> str:
    """
    Simplifies an absolute file path (Unix-style) to its canonical form.
    Handles multiple slashes '//', current directory '.', and parent directory '..'.
    Uses a Stack to efficiently process the current directory hierarchy.
    """
    stack = []
    directory = ''
    
    # Appending '/' guarantees the final directory name is processed when we reach the end of the loop.
    for i in path + '/':
        if i == '/':
            # We hit a separator, meaning we finished reading a name segment.
            if directory == '..':
                # '..' means "go up one level", so we pop from the stack if it isn't empty.
                if len(stack) != 0:
                    stack.pop()
            # We ignore '.' (current directory) and '' (empty strings caused by '//').
            # Anything else is a valid folder name, so we add it to the stack!
            elif directory != '.' and directory != '':
                stack.append(directory)
                
            # Reset our temporary string buffer to catch the next directory name.
            directory = ''
        else:
            # Keep building the directory name character-by-character.
            directory += i
            
    # (Note: Because of `path + '/'` in the loop above, `directory` will always be `''` here, 
    # making this bottom check practically redundant, but keeping it ensures safety).
    if directory == '..':
        if len(stack) != 0:
            stack.pop()
    elif directory != '.' and directory != '':
        stack.append(directory)
        
    # Reconstruct the canonical path by joining the valid directories with slashes.
    return '/' + '/'.join(stack)

def main():
    path = "/..//_home/a/b/..///"
    print(simplifyPath(path))

if __name__ == "__main__":
    main()
