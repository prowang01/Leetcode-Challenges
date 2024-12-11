# 347. Top K Frequent Elements

## Description
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in **any order**.

### Example 1:
**Input:**  
`nums = [1, 1, 1, 2, 2, 3]`, `k = 2`  
**Output:**  
`[1, 2]`  

### Example 2:
**Input:**  
`nums = [1]`, `k = 1`  
**Output:**  
`[1]`

### Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k is in the range [1, number of unique elements in the array].
- It is guaranteed that the answer is **unique**.


---

## Complexity
- **Runtime:** 52 ms  
- **Memory Usage:** 20.47 MB  

---

## Approach
Using a dictionary (`defaultdict`) to count the frequency of each element in `nums`. Then, iteratively select the `k` most frequent elements by finding the maximum key in the dictionary and removing it after each selection.

---

## Code
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in range (len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
        result = []
        for j in range(k):
            maxi = max(count, key = count.get)
            result.append(maxi)
            del (count[maxi])
        return result
