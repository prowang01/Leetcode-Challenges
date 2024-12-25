from collections import Counter

# Approach : Sliding Window
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Step 1: Initialize variables
        if not s or not t:  # Edge case
            return ""
        
        # Frequency map for t
        t_count = Counter(t)
        # To track current window's characters
        window_count = {}
        
        have, need = 0, len(t_count)  # `need` is the number of unique characters in t
        left = 0  # Left pointer for sliding window
        result = float("inf"), None, None  # To store the smallest window (length, start, end)
        
        # Step 2: Expand the window using the right pointer
        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1  # Update window count
            
            # If the character count matches in window and t
            if char in t_count and window_count[char] == t_count[char]:
                have += 1
            
            # Step 3: Shrink the window from the left if it's valid
            while have == need:
                # Update the result if the window is smaller
                if (right - left + 1) < result[0]:
                    result = (right - left + 1, left, right)
                
                # Remove the left character from the window
                window_count[s[left]] -= 1
                if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1  # Move left pointer forward
        
        # Step 4: Return the smallest window or empty string
        length, start, end = result
        return s[start:end+1] if result[1] is not None else ""





        '''
        Difficulties :

        1. What is Counter ? 
        2. Know all the steps to succeed with the sliding window
        3. Manipulating two dictionaries is tricky.

        etc.

        Runtime : 71 ms
        Memory : 18.46 MB
        
        '''