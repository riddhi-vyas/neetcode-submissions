#Time comp: O(n), Space comp: O(n)
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        #Initialize a bucket with all vals = 0, and length of bucket should be n+1 (0,1,,,n)
        bucket = [0]*(n+1)
        nums_map = Counter(nums) #freq map for item in nums
        for item, freq in nums_map.items():
            if bucket[freq] == 0: #case1: if bucket has no elements than 0
                bucket[freq] = [item]
            else: #case2: if bucket already has some elements other than 0
                bucket[freq].append(item)
        result = []
        for i in range(n, -1, -1): #traverse bucket reversely to get top k elements
            if len(result) != k and bucket[i] != 0:
                result.extend(bucket[i])
        return result