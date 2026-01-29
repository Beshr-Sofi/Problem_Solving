def groupAnagrams(strs):
    """
    Groups anagrams together from a list of words.
    
    This function iterates through each word, compares it with remaining words 
    by sorting their characters, and groups words with matching sorted characters 
    (anagrams) into sublists.
    
    Args:
        strs (list): A list of words/strings to group by anagrams
        
    Returns:
        list: A list of lists where each sublist contains all anagrams found in the input
    """
    tmp = []
    res = []
    end = len(strs)
    i = 0
    while i < end:
        j = i + 1
        tmp.append(strs[i])
        while j < end:
            if j < end  and sorted(strs[i]) == sorted(strs[j]):
                tmp.append(strs[j])
                strs.pop(j)
                end -= 1
            else:
                j += 1  
        res.append(tmp.copy())
        tmp.clear()
        i += 1
    return res

def main():
    """
    Main function that demonstrates the groupAnagrams function.
    
    Runs the groupAnagrams function on a sample list of words and prints 
    the grouped results to the console.
    """
    input_data = ["act","pots","tops","cat","stop","hat"]
    result = groupAnagrams(input_data)
    print(result)

if __name__ == "__main__":
    main()
