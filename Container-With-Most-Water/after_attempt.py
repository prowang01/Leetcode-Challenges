# Approach : using two pointers to test all the pairs.
# While calculating areas for each of the pairs
# And return the max

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxi = 0
        while l < r:
            current = min(height[l], height[r]) * (r-l)
            if current > maxi :
                maxi = current

            if height[l] < height[r]:
                l += 1
            else : 
                r -= 1
        return maxi
        

'''

We move the pointer where the height of the line is inferior to the other
Even when the pointers got the same height, with the strict operator
We still have to move on of the two pointers.

Runtime : 66 ms
Memory Usage : 27.90 MB

Complexity ? 
Time : O(n) because we only loop as long as l < r. In the worst case, it processes all n lines.
Space : O(1). We only use two constant variables : l and r.


Detailed Explanation : 

Time Complexity:

The algorithm uses a two-pointer technique:
The pointers start at the two ends of the array and move towards the center.
Each pointer is moved at most once for every iteration of the while loop.
Since the while loop runs while l < r, and l and r traverse the array only once, the time complexity is O(n), where n is the number of elements in height.

Space Complexity:

The algorithm uses a constant amount of extra space:
Variables like l, r, maxi, and current are used, which are all O(1) in space.
No additional data structures are used.
Therefore, the space complexity is O(1).

Comments : 

It was hard to understand the problem at first. I used the help of GPT to only get the intuition, and the methods to attack the problem.
The brute method was fine, I didn't need much help.
I needed more intuition infos (so more time) to solve the problem using the two-pointers method.
I didn't find the formula to calculate the area myself...



'''