#Approach: take left and right array -> multiply both to get result array
#answer[i] = product of everything LEFT of i
        #  × product of everything RIGHT of i
#Time comp: O(n)
# Space comp: O(1) ->Extra space is O(1), excluding the output array, because I reuse the output array to store the left products and maintain the right product in a single variable.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        left = [1]*n
        #create left array by multiplying elements from left of current item
        for i in range(1,n):
            left[i] = left[i-1]*nums[i-1]
        #Proceed to multiply product from right side
        #right_prod mean -> product of all elements strictly to the right of curent index i
        right_prod = 1 #multiplicative property
        for i in range(n-1,-1,-1):
            left[i] *= right_prod #step1 -> update left[i]
            right_prod *= nums[i] #step2 -> update right_prod
        return left