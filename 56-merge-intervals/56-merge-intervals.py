class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for l,r in intervals:
            if not ans:
                ans.append([l,r])
            else:
                if l <= ans[-1][-1]:
                    ans[-1][1] = max(r,ans[-1][1] )
                else:
                    ans.append([l,r])
                    
        return ans