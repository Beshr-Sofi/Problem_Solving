# Verify Alien Dictionary Order

## Problem Statement

In an alien language, the characters follow a specific ordering defined by the 'order' string.
Given a list of words and the alien alphabet order, determine if the words are sorted
according to the alien language's alphabetical order.

## Problem Breakdown

1. You have an 'order' string that defines how characters are ordered in the alien language
2. You need to check if a list of 'words' is sorted according to this alien order
3. Return True if sorted correctly, False otherwise

## Key Insights

- Compare consecutive words to find the first differing character
- When characters differ, check if they're in the correct order according to 'order'
- If a word is a prefix of the next word but longer, it's out of order (e.g., "apple" before "app")

## Algorithm

1. Create a mapping of each character to its position in the alien order
2. For each pair of consecutive words:
   - Compare characters position by position
   - When characters differ, check if they're in correct order using the mapping
   - If not in correct order, return False
   - If they match, move to the next pair
3. If all pairs are correctly ordered, return True

## Complexity Analysis

- **Time Complexity**: O(N \* L) where N is the number of words and L is the average length
- **Space Complexity**: O(1) since the order string is always 26 characters maximum

## Edge Cases

- Longer word comes before its prefix (invalid)
- Words are identical (valid, continue)
- Single word (valid, always sorted)
