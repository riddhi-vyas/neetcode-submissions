class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or not k:
            return []
        nums_map = Counter(nums)
        bucket = [0]*(len(nums)+1)
        for item, freq in nums_map.items():
            if bucket[freq] == 0:
                bucket[freq] = [item]
            else:
                bucket[freq].append(item)
        top_items = []
        n = len(nums)
        for i in range(n,-1,-1):
            if len(top_items) != k and bucket[i] != 0:
                top_items.extend(bucket[i])
        return top_items