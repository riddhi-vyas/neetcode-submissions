#Time comp: O(logn), space comp: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 0
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]: #min item is on right side of mid
                left = mid + 1
            else:
                right = mid
        return nums[right]