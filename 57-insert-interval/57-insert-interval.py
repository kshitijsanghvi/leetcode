class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        if newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]
        
        s = newInterval[0]
        e = newInterval[1]
        
        for i in range(len(intervals)):
            if s <= intervals[i][1]:
                left = s
                if s > intervals[i][0]:
                    left = intervals[i][0]
                j = i
                while j < len(intervals) and e > intervals[j][1]:
                    j += 1
                right = e
                if j == len(intervals):
                    return intervals[:i] + [[left,right]]
                if e == intervals[j][0]:
                    right = intervals[j][1]
                    return intervals[:i] + [[left,right]] + intervals[j+1:]
                if e >= intervals[j][0]:
                    right = intervals[j][1]
                    return intervals[:i] + [[left,right]] + intervals[j+1:]
                else:
                    return intervals[:i] + [[left,e]] + intervals[j:]
                    
        