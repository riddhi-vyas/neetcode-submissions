# Time comp:O(n^2) main loop iterates on n elements, sorting takes O(nlogn), Space comp: O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        n = len(nums)
        nums.sort()
        answer = []
        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    answer.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        return answer