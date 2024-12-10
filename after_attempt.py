''' 
Approach using a hash table : This approach counts the frequency of characters in one string and then adjusts the count by decrementing for the other string. 
If the strings are anagrams, the frequency of each character will cancel out, resulting in a map with all zero frequencies.

'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)
        for x in s : 
            count[x] += 1
        for x in t :
            count[x] -= 1
        
        for value in count.values():
            if value != 0 : 
                return False
        return True
