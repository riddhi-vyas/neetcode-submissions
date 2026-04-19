# logic
# 1. Edge Case: If the input array 'nums' is empty, return an empty array.
# 2. Setup:
#    - Find the length of 'nums' (let's call it 'n').
#    - Create an 'ans' array of size 'n', filled entirely with 1s.
# 3. First Pass (Calculate Left Products):
#    - Loop 'i' from 1 up to 'n - 1'.
#    - Set ans[i] = ans[i - 1] * nums[i - 1] 
#      (This stores the product of all elements to the left of index 'i').
# 4. Second Pass (Calculate Right Products & Combine):
#    - Initialize a variable 'right_prod' to 1 (keeps a running total of the right side).
#    - Loop 'i' backwards from 'n - 1' down to 0.
#    - Multiply the existing left product by the running right product: ans[i] *= right_prod
#    - Update the running right product with the current number: right_prod *= nums[i]
# 5. Result: Return the 'ans' array.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        ans = [1]*n
        # left array
        for i in range(1,n):
            ans[i] = ans[i-1]*nums[i-1]
        #right array
        right_prod = 1
        for i in range(n-1,-1,-1):
            ans[i] *= right_prod
            right_prod *= nums[i]
        return ans

#time comp: O(n)
#space comp: O(n)