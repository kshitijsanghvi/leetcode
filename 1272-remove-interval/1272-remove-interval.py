class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ans = []
        n = len(intervals)
        i = 0
        start = toBeRemoved[0]
        end = toBeRemoved[1]
        while i < n:
            if start >= intervals[i][1]:
                ans.append(intervals[i])
                i+=1
            else:
                if start > intervals[i][0]:
                    ans.append([intervals[i][0],start])
                else:
                    start = intervals[i][0]

                while i < n and end >= intervals[i][1]:
                        i += 1
                if  i < n and intervals[i][0] < end:
                    ans.append([end,intervals[i][1]])
                    i += 1
                
                while i < n:
                    ans.append(intervals[i])
                    i+=1

        return ans