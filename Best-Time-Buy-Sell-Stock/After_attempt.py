# Approach : Just taking two variables that will be refreshed when needed.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price, max_profit = float('inf'), 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price-min_price > max_profit:
                max_profit = price-min_price
        return max_profit

        
'''
Runtime : 19 ms
Memory Usage : 26.81 MB

We defined min_price at inf to update every value in the list 'array'
We compare max_profit everytime to ensure that the profit is okay.

Complexity :

Time complexity: O(n)

The algorithm iterates through the array of stock prices once, performing constant-time operations at each step. Therefore, the time complexity is linear in the size of the input array.

Space complexity: O(1)

The algorithm uses a constant amount of extra space to store variables like min_price and maxprof. The space complexity remains constant regardless of the size of the input array

'''