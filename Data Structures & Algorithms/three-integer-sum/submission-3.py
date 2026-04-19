class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # edge cases
        if not nums:
            return []
        # sort nums -> nlog(n)
        nums.sort()
        n = len(nums)
        result_list = []
        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]:  #to avoid duplicates of i
                continue
            j = i + 1
            k = n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    # update start ptr (j) to increase current total
                    j += 1
                elif total > 0:
                    # update end ptr (k) to decrease current total
                    k -= 1
                else: # total == 0
                    result_list.append([nums[i], nums[j], nums[k]])
                    # update both pointers
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]: # to avoid duplicates of j:
                        j += 1
                    while j < k and nums[k] == nums[k+1]: # to avoid duplicates of k
                        k -= 1
        return result_list
#time comp: O(n^2)
#space comp: O(1)