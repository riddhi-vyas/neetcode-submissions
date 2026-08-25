#Time comp: O(n), Space comp: O(1)
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        max_area = float('-inf')
        n = len(heights)
        L = 0
        R = n-1
        while L < R:
            #area = height * width
            curr_area = min(heights[L], heights[R]) * (R - L)
            max_area = max(curr_area, max_area)
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return max_area