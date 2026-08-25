#Time comp: O(logn), Space comp: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            # search in left sub-array
            if nums[start] <= nums[mid]:
                if target < nums[start] or target > nums[mid]:
                    #it means target not in left sub-array -> search right sub-array
                    # update start
                    start = mid + 1
                else: # target in left sub-array -> upate end
                    end = mid - 1
            #search in right sub-array
            else:
                if target < nums[mid] or target > nums[end]:
                    #it means target not in right sub-array -> search left sub-array
                    # update end
                    end = mid - 1
                else: #target in right sub-array -> update start
                    start = mid + 1
        return -1