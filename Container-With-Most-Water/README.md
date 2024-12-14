# 11. Container With Most Water

## Description

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the **maximum amount of water** a container can store.

### Example 1:

![Container with most water](Example1.jpg)

**Input:** height = [1,8,6,2,5,4,8,3,7]  
**Output:** 49  
**Explanation:** The above vertical lines represent the array `height`. The blue area is the maximum water that can be contained, which equals `49`.

### Example 2:
**Input:** height = [1,1]  
**Output:** 1  

### Constraints:
- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

---

## Approach
**Two Pointers Technique:**  
- Initialize two pointers: one at the leftmost index and one at the rightmost index.  
- Calculate the area formed by the vertical lines pointed to by the two pointers.  
- Move the pointer pointing to the shorter line inward to explore potentially larger areas.  
- Continue until the two pointers meet, keeping track of the maximum area encountered.

---

## Code
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxi = 0
        while l < r:
            current = min(height[l], height[r]) * (r-l)
            if current > maxi:
                maxi = current
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxi

```

## Complexity
- **Runtime:**  
  66 ms
- **Memory Usage:**  
  27.90 MB

### Time Complexity:
1. The while loop iterates through the array with two pointers, each moving toward the center, which takes O(n).
2. Calculations and comparisons within the loop are O(1).
**Overall:** **O(n)**.

### Space Complexity:
1. Only a constant amount of extra space is used for variables like l, r, maxi, and current.
**Overall:** **O(n)**.


