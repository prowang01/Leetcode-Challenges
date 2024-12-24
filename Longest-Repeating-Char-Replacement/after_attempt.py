# Approach : Sliding Window Left Right
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_length = 0  # To store the result
        char_count = {}  # Frequency map

        for right in range(len(s)):
            # Add the current character to the frequency map
            char_count[s[right]] = char_count.get(s[right], 0) + 1

            # Check if the current window is valid
            while (right - left + 1) - max(char_count.values()) > k:
                # Shrink the window by moving the left pointer
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]  # Clean up zero-frequency characters
                left += 1

            # Update the maximum length
            max_length = max(max_length, right - left + 1)

        return max_length


"""

Time Complexity:

- Iterating over the string: O(n), where n is the length of the string.
- Maintaining the frequency map: O(1), as it's bounded by 26 English letters.
- Overall: O(n).

Space Complexity:
- The frequency map stores at most 26 keys: O(1).

Runtime : 179 ms
Memory : 18 MB


NB : no need to actually change the characters, the goal is just to stay in the valid window without 
exceeding k.
In this context, sliding window is still hard, and i've had a hard time manipulating the dictionary.
"""
