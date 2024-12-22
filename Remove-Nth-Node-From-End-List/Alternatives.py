'''
Value-Shifting - AC in 64 ms

My first solution is "cheating" a little. Instead of really removing the nth node, I remove the nth value. I recursively determine the indexes (counting from back), then shift the values for all indexes larger than n, and then always drop the head.
'''

# Both solutions were just analyzed, I didn't try to experiment, just understanding the concept.

class Solution:
    def removeNthFromEnd(self, head, n):
        def index(node):
            if not node:
                return 0
            i = index(node.next) + 1
            if i > n:
                node.next.val = node.val
            return i
        index(head)
        return head.next

# Runtime : 3 ms
# Memory Usage : 17.88 MB

'''
Index and Remove - AC in 56 ms

In this solution I recursively determine the indexes again, but this time my helper function removes the nth node. It returns two values. The index, as in my first solution, and the possibly changed head of the remaining list.
'''

class Solution:
    def removeNthFromEnd(self, head, n):
        def remove(head):
            if not head:
                return 0, head
            i, head.next = remove(head.next)
            return i+1, (head, head.next)[i+1 == n]
        return remove(head)[1]

# Runtime : 0 ms
# Memory : 17.96 MB

# We have a readme explaining the concept super easily in the repository
