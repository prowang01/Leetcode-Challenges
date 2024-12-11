class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in range (len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
        result = []
        for j in range(k):
            maxi = max(count, key = count.get)
            result.append(maxi)
            del (count[maxi])
        return result

# max cannot be a variable name (because it's a method), so we called the max value 'maxi'
# we're not deleting from the list to go through the loop again, we directly test from the hash table
# and we don't delete the value, we delete the key.

'''
nums = [n for n in nums if n != max_freq]

Can reduce the list like that just to take the list without the most frequent number value.

'''
