# logic - binary search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        n = len(nums)
        end = n-1
        while start <= end:
            mid = (start+end)//2
            if target == nums[mid]:
                return mid
            # search in left sub-array
            if nums[start] <= nums[mid]:
                if target < nums[start] or target > nums[mid]:
                    #means target not in left sub-array -> it's in right side
                    # update start
                    start = mid + 1
                else:
                    # means target in left sub-array -> update end
                    end = mid-1
            # serach in right-subarray
            else:
                if target < nums[mid] or target > nums[end]:
                    # means target not in right array -> its in left array
                    # update end
                    end = mid -1
                else:
                    #means target in right sub-array -> update start
                    start = mid + 1
        return -1
#time comp: O(logn)
#space comp: O(1)