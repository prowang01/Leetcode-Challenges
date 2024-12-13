class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.split()
        s = ''.join(s)
        punc = '.:;/!?@#_,'
        for char in punc:
            s = s.replace(char, "")


'''

THIS APPROACH CANNOT BE USED, we need to really take all the non-alphanumeric characters.
It's a struggle not to forget any extras, so we'll abandon the idea.

'''



# Approach : two-pointers method
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l<r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1; r -= 1
        return True


'''
Runtime : 7 ms
Memory Usage : 17.48 MB

'''

# Complexity Analysis:
# Time Complexity:
# - The outer while loop runs as long as l < r. In the worst case, it processes all n characters.
# - The inner while loops skip non-alphanumeric characters. Each character is processed at most once.
# - Character comparisons are performed at most n/2 times (for valid characters).
# - Overall, the algorithm processes the string in linear time: O(n).

# Space Complexity:
# - The algorithm uses only two pointers (l and r) and no additional data structures.
# - This results in constant space usage: O(1).

# Summary:
# - Time Complexity: O(n)
# - Space Complexity: O(1)


'''


The "Two Pointers" technique is an algorithmic approach frequently used for solving problems involving arrays or strings. It leverages two indices (or pointers), typically named `l` (left) and `r` (right), which move towards the center from opposite ends of the structure.

This method is particularly effective when the problem involves comparisons between elements from both ends of the structure.


1. Initialization of Two Pointers:
   - `l` is initialized to `0` (the start of the string).
   - `r` is initialized to `len(s) - 1` (the end of the string).

2. Outer While Loop:
   - The main loop continues as long as `l < r`. This ensures the pointers do not cross or exceed their valid range.

3. Inner While Loops:
   - These loops are used to skip over non-alphanumeric characters:
     - The left pointer `l` moves forward until it points to an alphanumeric character or until `l >= r`.
     - The right pointer `r` moves backward until it points to an alphanumeric character or until `l >= r`.

4. Character Comparison:
   - After skipping non-alphanumeric characters, the characters at positions `l` and `r` are compared.
   - If the characters are not equal (after converting both to lowercase), the function immediately returns `False` because the string is not a palindrome.

5. Pointer Movement:
   - If the characters are equal, the pointers move closer to the center:
     - `l` is incremented to check the next character on the left.
     - `r` is decremented to check the next character on the right.

6. Final Return:
   - If the loop completes without finding unequal characters, the function returns `True`, indicating that the string is a palindrome.


'''
