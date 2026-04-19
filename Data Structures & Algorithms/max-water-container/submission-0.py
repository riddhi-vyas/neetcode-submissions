#logic: simply find area of rectangle the container makes, consider short bar for height
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
            height = min(heights[left], heights[right])
            length = right - left
            area = height*length
            max_area = max(area, max_area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area
#time comp: O(n)
#space comp:O(1)