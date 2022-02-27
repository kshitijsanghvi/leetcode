class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        
        """
        Word1 tp Word2
        """
        @lru_cache(None)
        def helper(i,j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            # Insert Delete Substitute
            return min(1 + helper(i,j+1),1 + helper(i+1,j),helper(i+1,j+1)+int(word1[i]!=word2[j]))
                
        return helper(0,0)