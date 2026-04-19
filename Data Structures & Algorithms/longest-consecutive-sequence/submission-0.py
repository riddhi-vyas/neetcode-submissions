#logic: Using Set data structure
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = 0
        nums_set = set(nums) #create a set to avoid duplicates in nums
        for num in nums_set:
            if (num-1) not in nums_set:
                num_next = num + 1
                length = 1
                while num_next in nums_set:
                    length += 1
                    num_next += 1
                longest = max(length, longest)
        return longest
#time complexity = O(n), space complexity = O(n)