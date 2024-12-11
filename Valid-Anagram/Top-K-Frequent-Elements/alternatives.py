class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] = frequency[num] + 1
        
        frequency = dict(sorted(frequency.items(), key = lambda x: x[1], reverse = True))
        result = list(frequency.keys())[:k]
        return result

'''

Runtime : 3 ms
Memory Usage : 20.51 MB


Explanations :
1. sorted() returns a list:

The sorted() function in Python always returns a list.
When applied to frequency.items(), it returns a list of tuples (key, value) sorted based on the specified criteria.

2. items() returns key-value pairs:

The frequency.items() method generates a view of all the key-value pairs in the dictionary.

3. lambda x: x[1] for sorting by values

4. reverse=True for descending order

'''



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        counter={}
        for n in nums:
            counter[n] = 1 + counter.get(n,0)
        
        for key, val in counter.items():
            heapq.heappush(heap, (-val,key))
        
        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        
        return res


'''

Runtime : 3 ms
Memory Usage : 20.57 MB

1. counter[n] = 1 + counter.get(n, 0): Iterate through each number n in nums and update its frequency in the counter dictionary. If n is not already in counter, counter.get(n, 0) returns 0, so counter[n] becomes 1. If n is already in counter, it increments its count by 1.

2. Problem here is in Python heap is usually min heap, so if we pop data from heap, we will get (1, 30) at first. Next time we will get (2, 10).

My strategy is when we add tuples to heap, we add negative to all frequency, so that maximum frequency will be minimum number.

For example,

(3, 20) → (-3, 20)
(2, 10) → (-2, 10)
(1, 30) → (-1, 30)
If we add negative to all frequency, min heap will work as a max heap.

(We're using the heap methode approach)

3. res: Initialize an empty list to store the top k frequent elements.
heapq.heappop(heap): Pop the smallest element from the heap (which is the one with the highest frequency due to the negative sign). The [1] retrieves the actual element (not its frequency) from the tuple (-val, key).
while len(res) < k: Continue extracting elements from the heap until we have k elements in res.

'''
