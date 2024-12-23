# 121. Best Time to Buy and Sell Stock

## Description
You are given an array `prices` where `prices[i]` is the price of a given stock on the \(i^{th}\) day.  
You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.  

Return the **maximum profit** you can achieve from this transaction.  
If you cannot achieve any profit, return `0`.

---

## Examples

### Example 1:
**Input:**  
`prices = [7,1,5,3,6,4]`  
**Output:**  
`5`  
**Explanation:**  
Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = \(6 - 1 = 5\).  
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

---

### Example 2:
**Input:**  
`prices = [7,6,4,3,1]`  
**Output:**  
`0`  
**Explanation:**  
In this case, no transactions are done, and the max profit = \(0\).

---

## Constraints:
- The length of the array is between 1 and 100,000 inclusive.
- Each price in the array is between 0 and 10,000 inclusive.


---

## Approach

### Steps:
1. **Track Minimum Price So Far:**  
   - As you iterate through the array, track the smallest price seen so far to simulate "buying" at the lowest price.
   
2. **Calculate Profit:**
   - For each price in the array, calculate the profit if you were to sell on that day:
     `profit = current_price - min_price_so_far`


3. **Update Maximum Profit:**  
   - Compare the calculated profit with the maximum profit seen so far and update it if necessary.

4. **Edge Case:**  
   - If the array is strictly decreasing (e.g., `[7, 6, 4, 3, 1]`), the profit will always be \( \leq 0 \), and the result will naturally be `0`.

---

## Code
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit


```

---

## Complexity
- **Runtime:**  
  19 ms
- **Memory Usage:**  
  26.81 MB

### Time Complexity:
**Overall:** **O(n)**.

### Space Complexity:

**Overall:** **O(1)**.


# Notes:
- The algorithm ensures that the **"buy" day always comes before the "sell" day** by tracking the minimum price seen so far.
- It naturally handles the case where **no profit is possible**, as the profit will never exceed `0` in such scenarios.
- The approach is efficient, making it suitable for large input sizes up to 100,000.
