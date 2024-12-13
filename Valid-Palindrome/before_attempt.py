# Approach : put the letters in lowercase, split to remove the spaces and then join to gather again,
# Make a list of all the punctuations possible, and then go through a loop and remove the extras non-alphanumeric characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.split()
        s = ''.join(s)
        punc = '.:;/!?,'
        for i in range (len(punc)):
            for y in range (len(s)):
                if (punc[i] == s[y]):
                    s = s.replace(s[y],"")
        return s
      

'''
All the issues :
1. Didn't know that we can't browse the elements in a string; it's different from the lists,
so use the indexes.
2. I didn't know how to remove an element from a string.
3. I still don't know how to remove the punctuations, everything else was done,
putting the letters in a lowercase, removing the spaces.


THIS APPROACH CANNOT BE USED, we need to really take all the non-alphanumeric characters.
It's a struggle not to forget any extras, so we'll abandon the idea.

'''