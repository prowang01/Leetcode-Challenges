class Solution:
    # Approach : Optimized Sliding Window
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        char_set = set() # to see if characters are repeated or not
        max_length = 0
        for right in range(len(s)):  # sliding the right window to add characters
            while s[right] in char_set:  # veryfing the repetition
                char_set.remove(s[left])   # sliding left window to make a new valid substring 
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length

'''
Original Approach given by GPT
Runtime : 11 ms
Memory : 17.66 MB

'''

# Complexity:

# Time Complexity:

# 1. The right pointer iterates through the string once -> O(n)
# 2. The left pointer also iterates through the string at most once -> O(n)
# 3. Total Time Complexity: O(n)
    
# Space Complexity:

# 1. The set `char_set` stores up to n characters (in the worst case, all unique).
# 2. Total Space Complexity: O(n)
