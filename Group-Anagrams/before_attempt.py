# Approach : sort the words in an alphabetically order first in a new list...
# ...then compare each element of this list,
# if equal, get the words -> not a wise approach

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        L = []
        for x in strs:
            s = sorted(x)
            L.append(s)
        return L


     