# Invariant: 1)find i, j such that i!=j and nums[i]+nums[j] = target
# Approach: Hashmap storing num: index
# Time comp: O(N), Space comp: O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        nums_map = {}
        for i in range(len(nums)):
            if target - nums[i] not in nums_map:
                nums_map[nums[i]] = i
            else:
                return [nums_map[target - nums[i]], i]