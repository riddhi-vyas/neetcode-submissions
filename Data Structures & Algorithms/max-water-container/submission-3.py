#Time comp: O(n), Space comp: O(1)
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        max_area = float('-inf')
        start = 0
        end = len(heights) - 1
        while start < end:
            #area = length * height
            curr_area = (end-start) * min(heights[start], heights[end])
            max_area = max(curr_area, max_area)
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        return max_area