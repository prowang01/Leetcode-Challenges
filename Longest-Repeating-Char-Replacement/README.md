# 424. Longest Repeating Character Replacement

## Description
You are given a string `s` and an integer `k`.  
You can choose any character of the string and change it to any other uppercase English character.  
You can perform this operation at most `k` times.  

Return the **length of the longest substring** containing the same letter you can get after performing the above operations.

---

## Examples

### Example 1:
**Input:**  
`s = "ABAB", k = 2`  
**Output:**  
`4`  
**Explanation:**  
Replace the two 'A's with two 'B's or vice versa.

---

### Example 2:
**Input:**  
`s = "AABABBA", k = 1`  
**Output:**  
`4`  
**Explanation:**  
Replace the one 'A' in the middle with 'B' to form `"AABBBBA"`.  
The substring `"BBBB"` has the longest repeating letters, which is `4`.

---

## Constraints:
- 1 <= s.length <= 100000
- `s` consists of only uppercase English letters.
- 0 <= k <= s.length

---

## Approach: Sliding Window

This problem can be solved using the Sliding Window approach to maintain the longest valid substring.

### Steps:
1. **Track Character Frequencies:**
   - Use a dictionary to store the frequency of each character within the current window.

2. **Expand the Window:**
   - Increase the window size by moving the `right` pointer.

3. **Check Validity of the Window:**
   - The substring is valid if:  
     (Window Size) - (Most Frequent Character Count) <= k  
     - Window Size = `right - left + 1`
     - Most Frequent Character Count is the count of the most frequent character in the window.
   - If the condition fails, shrink the window by moving the `left` pointer.

4. **Update the Maximum Length:**
   - Keep track of the maximum length of the valid substring.

---

## Code:

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_length = 0
        char_count = {}

        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1

            while (right - left + 1) - max(char_count.values()) > k:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            max_length = max(max_length, right - left + 1)

        return max_length


```



## Complexity

### Time Complexity:
- Iterating over the string: **O(n)**, where `n` is the length of the string.
- Updating the frequency map is **O(1)** as it only involves at most 26 English letters.
- **Overall:** **O(n)**.

### Space Complexity:
- The frequency map stores at most 26 keys: **O(1)**.
- **Overall:** **O(1)**.

---

## Notes:
- This algorithm dynamically adjusts the window size based on the constraints (`k` replacements).
- The use of a frequency map ensures that character counts are efficiently tracked within the window.
- The solution is optimal for large strings due to its linear time complexity.
