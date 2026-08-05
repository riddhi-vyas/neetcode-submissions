class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #edge case
        if not nums:
            return []
        nums_map = {}
        for i in range(len(nums)):
            if target - nums[i] not in nums_map:
                nums_map[nums[i]] = i
            else:
                return [nums_map[target - nums[i]], i]