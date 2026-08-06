class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        #left
        left = [1]*n
        for i in range(1,n):
            left[i] = left[i-1]*nums[i-1]
        #right
        right_prod = 1
        for i in range(n-1,-1,-1):
            left[i] *= right_prod
            right_prod *= nums[i]
        return left