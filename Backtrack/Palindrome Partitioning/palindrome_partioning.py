r"""
Problem:
    Given a string s, partition s such that every substring of the partition
    is a palindrome. Return all possible palindrome partitionings of s.

Backtracking Logic:
    1. Decision at step 'index':
       - Try every possible substring cut s[index : i + 1] for i in range(index, len(s)).
    2. Prune (Check Validity):
       - If s[index : i + 1] is NOT a palindrome, skip it (do not explore deeper).
    3. Choose & Recurse:
       - If s[index : i + 1] is a palindrome, add it to 'current_partition'.
       - Recursively explore the remaining string starting from index 'i + 1'.
    4. Backtrack:
       - Remove the last added substring (current_partition.pop()) to explore
         other cut lengths from the same starting index.
    5. Base Case:
       - When index == len(s), the entire string has been successfully partitioned
         into valid palindromes. Append a copy of current_partition to result.

Decision Tree Example (s = "aab"):

                                      "" [index=0]
                       /                   |                  \
                  cut="a"               cut="aa"            cut="aab"
                [Palindrome]          [Palindrome]        [Not Palindrome]
                     /                     |                     \
              index=1                   index=2                  [X]
             /       \                     |
         cut="a"    cut="ab"            cut="b"
        [Palin.]    [Not Palin.]       [Palin.]
           /            \                  |
       index=2          [X]             index=3 (Base Case!)
          |                                |
       cut="b"                        Result: ["aa", "b"] ✅
       [Palin.]
          |
       index=3 (Base Case!)
          |
       Result: ["a", "a", "b"] ✅

Complexity:
    - Time Complexity:  O(N * 2^N), where N = len(s).
                        There are 2^(N-1) possible partitions of a string of length N.
                        For each partition, palindrome verification takes O(N).
    - Space Complexity: O(N) for recursion stack depth and current_partition storage.
"""


def is_palindrome(s):
    """Check if string s reads the same forwards and backwards."""
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True


def palindrome_partitioning(s):
    """Generate all possible palindrome partitionings of s."""
    result = []

    def backtrack(index, current_partition):
        # Base case: reached the end of the string
        if index == len(s):
            result.append(list(current_partition))
            return

        # Try every potential cut from 'index' to 'i'
        for i in range(index, len(s)):
            substring = s[index:i + 1]
            # Pruning: only explore branches where the current substring is a palindrome
            if is_palindrome(substring):
                current_partition.append(substring)  # Choose
                backtrack(i + 1, current_partition)   # Explore
                current_partition.pop()               # Backtrack (Unchoose)

    backtrack(0, [])
    return result


def main():
    test_cases = ["aab", "a", "racecar"]
    for word in test_cases:
        print(f"Partitioning '{word}': {palindrome_partitioning(word)}")


if __name__ == "__main__":
    main()
