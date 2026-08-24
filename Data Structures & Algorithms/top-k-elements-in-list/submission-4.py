# Bucket sort: keys are freq(count), values are the actual numbers
# Time comp: O(n), space comp: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        nums_map = Counter(nums)
        bucket = [0]*(len(nums)+1)
        for item, freq in nums_map.items():
            if bucket[freq] == 0: #bucket is empty initially
                bucket[freq] = [item] #create new bucket with k:v -> freq:item
            else: #bucket already exists with current freq -> append item
                bucket[freq].append(item)
        #traverse bucket reversely (because bucket starts from freq: 0,1,2....n)
        n = len(nums)
        top_items = []
        for i in range(n,-1,-1):
            if len(top_items) != k and bucket[i] != 0:
                top_items.extend(bucket[i])
        return top_items