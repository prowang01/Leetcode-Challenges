# Approach using a tuple to play the key role in the hash map 
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters_to_words = defaultdict(list)
        for word in strs:
            letters_to_words[tuple(sorted(word))].append(word)
        return list(letters_to_words.values())

'''
What types can be used as keys in a Python dictionary?
For a type to be used as a key in a dictionary, it must be hashable and immutable:

Hashable:
An object is hashable if it has a hash value (calculated using the built-in hash() function) that does not change during its lifetime.

Immutable:
If an object can be modified after its creation (like a list), it cannot be used as a key, as its hash value could change.
'''
