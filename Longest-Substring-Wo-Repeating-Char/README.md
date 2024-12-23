# 3. Longest Substring Without Repeating Characters

## Description
Given a string `s`, find the length of the **longest substring** without repeating characters.

---

## Examples

### Example 1:
**Input:**  
`s = "abcabcbb"`  
**Output:**  
`3`  
**Explanation:**  
The answer is `"abc"`, with the length of `3`.

---

### Example 2:
**Input:**  
`s = "bbbbb"`  
**Output:**  
`1`  
**Explanation:**  
The answer is `"b"`, with the length of `1`.

---

### Example 3:
**Input:**  
`s = "pwwkew"`  
**Output:**  
`3`  
**Explanation:**  
The answer is `"wke"`, with the length of `3`.  
Notice that the answer must be a **substring**, `"pwke"` is a subsequence and not a substring.

---

## Constraints:
- \(0 \leq \text{s.length} \leq 5 \times 10^4\)
- `s` consists of English letters, digits, symbols, and spaces.

---

## Approach (Hint-Based)
### Steps:
1. **Generate All Substrings:**  
   Use a nested loop to generate substrings starting from every index of the string.
   
2. **Check Uniqueness:**  
   For each substring, check whether it contains unique characters. If a repeating character is found, stop extending the substring.

3. **Update Maximum Length:**  
   Keep track of the maximum length of all valid substrings encountered.

---

## Code
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0  

        for i in range(len(s)):  
            seen_characters = set()  
            for j in range(i, len(s)):  
                if s[j] in seen_characters: 
                    break  
                seen_characters.add(s[j])  
                max_length = max(max_length, j - i + 1)  

        return max_length

```

---

## Complexity

### Time Complexity:
1. **Outer Loop**:  
   - Runs \( n \) times, where \( n \) is the length of the string.

2. **Inner Loop**:  
   - Runs up to \( n \) times for each iteration of the outer loop.

3. **Checking Uniqueness**:  
   - For each substring, checking uniqueness using a set takes \( O(n) \) in the worst case.

4. **Total Time Complexity**:  
   - Combining the above, the total time complexity is **\( O(n^3) \)**.

---

### Space Complexity:
1. **Using a Set**:  
   - A set is used to store characters for each substring, which can store up to \( n \) characters in the worst case.
2. **Overall Space Complexity**:  
   - **\( O(n) \)**.

---

## Key Notes:
- This approach works but can become slow for larger strings due to the **\( O(n^3) \)** complexity.
- Let me know if you'd like to test this solution or move on to an optimized approach!
