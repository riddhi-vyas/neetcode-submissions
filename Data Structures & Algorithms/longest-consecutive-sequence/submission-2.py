# Time and Space comp: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = 0
        set_nums = set(nums)
        for num in set_nums:
            if (num-1) not in set_nums:
                length = 1
                next_num = num + 1
                while next_num in set_nums:
                    length += 1
                    next_num += 1
                longest = max(longest, length)
        return longest