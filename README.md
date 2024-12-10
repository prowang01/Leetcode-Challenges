# 242. Valid Anagram

## Description
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

### Example 1:
**Input:** s = "anagram", t = "nagaram"  
**Output:** true

### Example 2:
**Input:** s = "rat", t = "car"  
**Output:** false

### Constraints:
- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.


# Complexity
- Runtime :
20 ms

- Memory Usage :
18.24 MB


# Approach
Ordering alphabetically the two strings and comparing them

# Code
```python3 []
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t) : 
            A = sorted(s)
            B = sorted(t)
            if A == B :
                return True
            return False
        return False
        
```