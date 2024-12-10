'''
Approach using sorted strings
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t) : 
            A = sorted(s)
            B = sorted(t)
            if A == B :
                return True
            return False