"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        
        nums = []
        for i in schedule:
            n = len(i)
            for j in range(n):
                nums.append([i[j].start,-1])
                nums.append([i[j].end,1])
        
        nums.sort()
        count = 0
        start = None
        ans = []
        for time, state in nums:
            if state == -1:
                count += 1
                if count == 1:
                    if start:
                        ans.append(Interval(start,time))
                        
            elif state == 1:
                count -= 1
                if count == 0:
                    start = time
        return ans
                
            