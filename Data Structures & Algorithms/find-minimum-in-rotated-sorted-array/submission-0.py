#logic - binary search
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        start = 0
        end = n-1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]: # min_item is on second half of array
                # means min is after mid ptr -> update start
                start = mid + 1
            else: # min_item is on first half of array
                # means min is before mid ptr -> update end
                end = mid
        return nums[end]
#time comp: O(logn), n is length of input list
#space comp: O(1), only temp ptrs(start, mid, end) used -> doesn't require extra Data structures or memory proportional to input size