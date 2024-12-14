# Approach : Testing out all the pairs of lines existing and calculating their areas
# Then put all the results in a list and take the max
# Found this approach with GPT because the problem was hard to understand
# (Both the formula of the area, and this brute method came from GPT)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        areas = []
        for i in range(len(height)):
            for j in range (i+1, len(height)):
                ar = min(height[i], height[j])*(j-i)
                areas.append(ar)
        return max(areas)

'''
The problem results in the complexity, we know that this method is inefficient
O(n^2) because we got a nested loop.

'''