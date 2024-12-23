# Approach : Just taking two variables that will be refreshed when needed.
# Same concept : different approach
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy_price = prices[0]
        profit = 0
        for price in prices[1::]:
            if buy_price > price:
                buy_price = price
            profit = max(profit, price - buy_price)
        return profit
        
'''
Runtime : 95 ms
Memory Usage : 26.91 MB

We defined min_price at inf to update every value in the list 'array'
We compare max_profit everytime to ensure that the profit is okay.

Complexity :

Time complexity: O(n)

The algorithm iterates through the array of stock prices once, performing constant-time operations at each step. Therefore, the time complexity is linear in the size of the input array.

Space complexity: O(1)

The algorithm uses a constant amount of extra space to store variables like min_price and maxprof. The space complexity remains constant regardless of the size of the input array


Way Longer Runtime and more memory usage.

'''