# 76. Minimum Window Substring

## Description
Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window substring** of `s` such that **every character in `t`** (including duplicates) is included in the window.  
If there is no such substring, return the empty string `""`.

The test cases will be generated such that the answer is **unique**.

---

## Examples

### Example 1:
**Input:**  
`s = "ADOBECODEBANC", t = "ABC"`  
**Output:**  
`"BANC"`  
**Explanation:**  
The minimum window substring `"BANC"` includes `'A'`, `'B'`, and `'C'` from string `t`.

---

### Example 2:
**Input:**  
`s = "a", t = "a"`  
**Output:**  
`"a"`  
**Explanation:**  
The entire string `s` is the minimum window.

---

### Example 3:
**Input:**  
`s = "a", t = "aa"`  
**Output:**  
`""`  
**Explanation:**  
Both `'a'`s from `t` must be included in the window. Since `s` only has one `'a'`, return an empty string.

---

## Constraints:
- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 10^5`
- `s` and `t` consist of only English letters.

---

## Approach: Sliding Window

We use a **Sliding Window** approach to dynamically adjust the window size while ensuring all characters of `t` are present in the window.

### Steps:
1. **Track Target Frequencies:**  
   - Use `t_count` (a frequency map) to store the count of characters in `t`.

2. **Expand the Window (Right Pointer):**  
   - Add `s[right]` to the `window_count` map and check if the character meets the required count in `t_count`.

3. **Check Validity of the Window:**  
   - A window is valid if all characters in `t` meet or exceed the required count.

4. **Shrink the Window (Left Pointer):**  
   - Move the `left` pointer to minimize the window while maintaining validity.
   - Update the result if the current window is smaller than the previously recorded smallest window.

5. **Return Result:**  
   - Extract the substring using the start and end indices of the smallest window.

---

## Code

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        t_count = Counter(t)
        window_count = {}

        have, need = 0, len(t_count)
        result = float("inf"), None, None  
        left = 0

        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1

            if char in t_count and window_count[char] == t_count[char]:
                have += 1

            while have == need:
                if (right - left + 1) < result[0]:
                    result = (right - left + 1, left, right)

                window_count[s[left]] -= 1
                if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1

        length, start, end = result
        return s[start:end + 1] if length != float("inf") else ""

```

---

## Complexity

### Time Complexity:
1. **Iterating over `s`:**  
   - **O(m)**, where `m` is the length of `s`.
2. **Maintaining `window_count`:**  
   - **O(1)** (at most 26 letters for English characters).

**Overall:** **O(m)**.

---

### Space Complexity:
1. **Frequency maps (`t_count` and `window_count`):**  
   - **O(n)** for `t_count` and **O(1)** for `window_count`.

**Overall:** **O(n)**.

## Notes:
- The algorithm ensures the smallest valid window is found while maintaining linear complexity.
- Dynamically adjusting the window size avoids recomputation for each substring.
- Using a frequency map ensures efficient checks for character counts.
