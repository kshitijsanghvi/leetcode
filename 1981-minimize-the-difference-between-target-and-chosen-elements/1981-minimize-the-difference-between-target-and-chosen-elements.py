class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        m,n = len(mat),len(mat[0])
        
        for i in range(m):
            mat[i] = sorted(set(mat[i]))
        
        @lru_cache(None)
        def helper(r,s):
            if r == -1:
                return abs(target-s)
            
            ans = float('inf')
            for j in mat[r]:
                ans = min(ans,helper(r-1,s+j))
                if s + j >= target:
                    break

            return ans
        
        return helper(m-1,0)
        