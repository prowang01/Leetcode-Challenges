# 125. Valid Palindrome

## Description
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

### Example 1:
**Input:** s = "A man, a plan, a canal: Panama"  
**Output:** true  

### Example 2:
**Input:** s = "race a car"  
**Output:** false  

### Example 3:
**Input:** s = " "  
**Output:** true  

### Constraints:
- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

## Approach
**Using `.isalnum()` and reversing strings:**  
- Remove all non-alphanumeric characters using a generator with `isalnum()`.
- Convert the filtered string to lowercase with `.lower()`.
- Compare the string with its reversed version using slicing (`[::-1]`).

## Code
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum())
        return s.lower() == s.lower()[::-1]

```

## Complexity
- **Runtime:**  
  10 ms
- **Memory Usage:**  
  17.89 MB

### Time Complexity:
1. Filtering the string with `isalnum()` and joining takes **O(n)**.
2. Applying `.lower()` to the filtered string takes **O(n)**.
3. Reversing the string with slicing (`[::-1]`) takes **O(n)**.
4. Comparing the original string and the reversed string takes **O(n)**.  
**Overall:** **O(n)**.

### Space Complexity:
1. The filtered string created by `''.join()` requires **O(n)** space.
2. Applying `.lower()` creates another copy of the string, which takes **O(n)**.
3. Reversing the string creates another copy, taking **O(n)**.  
**Overall:** **O(n)**.


