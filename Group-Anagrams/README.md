# 49. Group Anagrams

## Description
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

### Example 1:
**Input:**  
`strs = ["eat", "tea", "tan", "ate", "nat", "bat"]`  
**Output:**  
`[["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]`

**Explanation:**  
- There is no string in `strs` that can be rearranged to form `"bat"`.
- The strings `"nat"` and `"tan"` are anagrams as they can be rearranged to form each other.
- The strings `"ate"`, `"eat"`, and `"tea"` are anagrams as they can be rearranged to form each other.

---

### Example 2:
**Input:**  
`strs = [""]`  
**Output:**  
`[[""]]`

---

### Example 3:
**Input:**  
`strs = ["a"]`  
**Output:**  
`[["a"]]`

---

### Constraints:
- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.


---

### Runtime and Memory Analysis:
1. **Time Complexity:**  
   - Sorting each word takes \(O(k \log k)\), where \(k\) is the length of the word.  
   - For \(n\) words, the total complexity is \(O(n \cdot k \log k)\).
2. **Space Complexity:**  
   - Storing the hashmap requires \(O(n \cdot k)\) for the grouped anagrams.

---

### Performance:
- **Runtime:** 7 ms  
- **Memory Usage:** 20.16 MB  

---

## Approach

### Using a HashMap:
1. **Sorting Words:**  
   - Each word is sorted alphabetically to create a "signature" for its anagram group.
   - For example, `"eat"`, `"tea"`, and `"ate"` all have the same sorted signature `"aet"`.
2. **HashMap Storage:**  
   - Use the sorted word as a key in a hashmap (`anagram_map`) and append the original word to its corresponding group.

--- 

## Code

```python
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for x in strs:
            word = ''.join(sorted(x))
            anagram_map[word].append(x)
        return list(anagram_map.values())
