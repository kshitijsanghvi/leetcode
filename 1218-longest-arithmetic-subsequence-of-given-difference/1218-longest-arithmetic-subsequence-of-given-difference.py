class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        d = {}
        ans = 0
        
        for i in arr:
            d[i] = d[i-difference] + 1 if (i - difference) in d else 1  
            ans = max(ans,d[i])
            
        return ans