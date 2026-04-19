class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #edge cases
        if not nums:
            return []
        nums_map = {} #this dict will have the number, idx from nums
        for idx in range(len(nums)):
            if target - nums[idx] not in nums_map:
                nums_map[nums[idx]] = idx
            else:
                return [nums_map[target - nums[idx]], idx]