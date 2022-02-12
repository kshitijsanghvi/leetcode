class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = intervals[0]
        remove = 0
        for l,r in intervals[1:]:
            if l < prev[-1]:
                if r < prev[-1]:
                    prev = [l,r]
                remove += 1
            else:
                prev = [l,r]
        return remove