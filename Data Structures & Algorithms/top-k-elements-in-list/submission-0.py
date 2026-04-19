import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #edge case
        if not nums or not k:
            return []
        nums_map = Counter(nums) # it will create a hashmap storing num, freq from nums
        bucket = [0]*(len(nums)+1) # freq-bucket where freq of num is keys for buckets, numbers will be the values inside that freq
        for item, freq in nums_map.items():
            if bucket[freq] == 0:
                bucket[freq] = [item] # if freq of curent item = 0 in bucket, add it as a new key in bucket with item as a value for that key(current freq)
            else:
                bucket[freq].append(item) # if bucket already have key for current freq, append item to this bucket as val
        top_elems = []
        n = len(nums)
        # iterate over bucket from back(Descending order to get top items)
        for i in range(n,-1,-1):
            if len(top_elems) != k and bucket[i] != 0:
                top_elems.extend(bucket[i])
        return top_elems