class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        
        @lru_cache(None)
        def helper(i,j):
            nonlocal n, m
            if i == n:
                return m - j
            if j == m:
                return n - i
            val = m + n
            if word1[i] == word2[j]:
                val = min(val , helper(i+1,j+1))
            val = min(val, 1 + helper(i+1,j), 1 + helper(i,j+1))
            
            return val
        
        return helper(0,0)