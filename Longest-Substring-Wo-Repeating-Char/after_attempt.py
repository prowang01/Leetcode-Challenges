class Solution:
    # Approach : brute force with a nested loop to generate substrings and check for repeated letters
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0 # our output
        for i in range(len(s)):
            seen_characters = set()
            for j in range(i, len(s)): # to avoid having subsequences
                if s[j] in seen_characters: # if the letter is repeating itself
                    break
                seen_characters.add(s[j])
                max_length = max(max_length, j-i+1) # Length of the substring / vs overall max_length
        return max_length

            

'''
Runtime : 507 ms
Memory : 17.81 MB

'''

# Complexity:
# 
# Time Complexity:
# 1. Outer loop runs n times, where n is the length of the string.
# 2. Inner loop runs up to n times for each iteration of the outer loop.
# 3. Checking uniqueness using a set takes O(n) in the worst case.
# 4. Total Time Complexity: O(n^3).
#
# Space Complexity:
# 1. A set is used to store characters for each substring, which can store up to n characters in the worst case.
# 2. Overall Space Complexity: O(n).
#
# Key Notes:
# - This approach works but can become slow for larger strings due to the O(n^3) complexity.
# - Consider an optimized approach (like Sliding Window) for better performance.
