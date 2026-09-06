#Approach: take left and right array -> multiply both to get result array
#answer[i] = product of everything LEFT of i
        #  × product of everything RIGHT of i
#Time comp: O(n)
# Space comp: O(1) ->Extra space is O(1), excluding the output array, because I reuse the output array to store the left products and maintain the right product in a single variable.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        left_prod = [1]*(len(nums))
        for i in range(1, len(nums)):
            left_prod[i] = left_prod[i-1] * nums[i-1]
        right_prod = 1
        for i in range(len(nums)-1, -1, -1):
            left_prod[i] = left_prod[i] * right_prod
            right_prod *= nums[i]
        return left_prod        