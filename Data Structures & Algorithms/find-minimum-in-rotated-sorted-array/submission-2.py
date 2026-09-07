#Time comp: O(logn), space comp: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        start = 0
        end = len(nums)-1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]: #if yes -> min is on right half on mid
                start = mid + 1
            else:
                end = mid
        return nums[end]