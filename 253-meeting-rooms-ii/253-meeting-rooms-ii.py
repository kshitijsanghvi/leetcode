class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = [[i[0],1] for i in intervals] + [[i[1],-1] for i in intervals]
        intervals.sort()
        ans = c = 0
        for i,s in intervals:
            if s == 1:
                c+=1
                ans = max(ans,c)
            else:
                c-=1
        return ans
        