#Time comp: O(N), Space comp = O(N)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        nums_map = {}
        for i in range(len(nums)):
            if nums[i] not in nums_map:
                nums_map[nums[i]] = 1
            else:
                return True
        return False