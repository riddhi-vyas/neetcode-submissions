#optimized code length (logic is same - rectangle area)
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #edge case
        if not heights:
            return 0
        n = len(heights)
        left = 0
        right = n-1
        max_area = float('-inf')
        while left < right:
            # area = length*height
            # length is distance between two bars
            area = min(heights[left], heights[right])*(right - left)
            max_area = max(area, max_area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area
#time comp: O(n)
#space comp:O(1)