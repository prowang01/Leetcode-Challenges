# Approach : sort the words in an alphabetically order first in a new list...
# ...then compare each element of this list,
# if equal, get the words -> not a wise approach

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for x in strs:
            word = ''.join(sorted(x))
            anagram_map[word].append(x)
        return list(anagram_map.values())

# Conclusion : the approach was wise, we just needed to change our tools -> hash map 
# So we still sort the words in an alphabetically order, but we join each letter because letters were separated in the first try.
# And we stock the sorted word as a key in the hash map,
# Then we add a word by assigning it to its own key (sorted word)
# And we only return the value, the hashmap being converted into a list to fill the requirement