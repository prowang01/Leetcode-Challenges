# Approach : using .isalnum() and comparing by reversing the strings.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum())
        return s.lower() == s.lower()[::-1]



''' 

.isalnum() is a new method to me.
.lower() too, it's to put letters in lowercase.

Runtime : 10 ms
Memory Usage : 17.89 MB

'''

# Time Complexity:
# - The comprehension inside ''.join() iterates through all characters in the string `s`
#   and checks if each character is alphanumeric, which takes O(n).
# - The .lower() method is applied to the entire filtered string, which also takes O(n).
# - The slicing operation [::-1] creates a reversed copy of the string, which is O(n).
# - Comparing the string with its reverse takes O(n).
# Overall, the time complexity is O(n).

# Space Complexity:
# - The ''.join() operation creates a new string containing only alphanumeric characters,
#   requiring O(n) space in the worst case (if all characters are alphanumeric).
# - The .lower() operation creates a copy of the filtered string, requiring O(n) space.
# - The slicing operation [::-1] creates another reversed copy of the string, requiring O(n) space.
# Overall, the space complexity is O(n).



