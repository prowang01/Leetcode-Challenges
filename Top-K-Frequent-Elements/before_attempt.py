# Before attempt : Try to count the frequency of the first most counted element (using a hash table)
# Then deleting it from the initial list and doing the same loop until the integer k is reached
# Doesn't work

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for j in range(1,k+1):
            for i in range (len(nums)):
                if nums[i] not in count:
                    count[nums[i]] = 1
                else:
                    count[nums[i]]+=1
            L = [max(count, key = count.get)]
            list.remove(max(count( key=count.get)))
        return L

