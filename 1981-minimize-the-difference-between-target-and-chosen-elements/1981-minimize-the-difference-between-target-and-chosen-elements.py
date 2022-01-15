class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        m, n = len(mat), len(mat[0])
        
        
        
        for i in range(m):
            mat[i] = sorted(set(mat[i]))
        
        @lru_cache(None)
        def helper(r,s):
            if r == m:
                return abs(s - target)

            ans = float('inf')
            for i in mat[r]:
                ans= min(ans,helper(r+1,s+i))
                if s + i >= target:
                    break                       
            return ans
        
        return helper(0,0)