# Longest Common Prefix

## Problem Statement

Given an array of strings, find the longest common prefix string amongst all the strings.
If there is no common prefix, return an empty string.

## Problem Breakdown

1. You have a list of 'strs' containing multiple strings
2. You need to find the longest prefix that appears at the beginning of all strings
3. Return the common prefix string, or empty string if none exists

## Key Insights

- Compare characters at the same position across all strings
- Stop as soon as a mismatch is found or a string ends
- The common prefix cannot be longer than the shortest string in the list
- If the first string is empty, there's no common prefix

## Algorithm

1. Use the first string as a reference for character positions
2. For each character position in the first string:
   - Check if all other strings have the same character at that position
   - If any string is shorter or has a different character, stop
   - Otherwise, add the character to the result
3. Return the accumulated common prefix

## Complexity Analysis

- **Time Complexity**: O(S) where S is the sum of all characters in all strings (worst case when all match)
- **Space Complexity**: O(1) excluding the output string

## Edge Cases

- Empty list of strings (undefined behavior, depends on implementation)
- Single string (the entire string is the prefix)
- Strings with no common prefix (returns empty string)
- One string is a prefix of another (returns the shorter one)
- All strings are identical (returns the entire string)
