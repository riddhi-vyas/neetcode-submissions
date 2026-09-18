#Time comp: O(n log n) due to sorting the intervals, where n is the number of intervals
#Space comp: O(n)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort() # nlogn complexity
        res = [intervals[0]] #initialize res list with first pair from intervals list
        for item in range(1, len(intervals)):
            if intervals[item][0] <= res[-1][1]: #items's start is < res's last item's end
                # need to merge item and prev item in res
                res[-1][1] = max(res[-1][1], intervals[item][1])
            else: #no overlapping
                res.append(intervals[item])
        return res