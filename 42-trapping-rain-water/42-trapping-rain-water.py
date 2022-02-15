class Solution:
    def trap(self, height: List[int]) -> int:
        
        dpr = {}
        dpl = {}
        n = len(height)
        def helperl(i):
            if i == -1:
                return float('-inf')
            if i not in dpl:
                dpl[i] = helperl(i-1) if height[i] < helperl(i-1) else height[i]
            return dpl[i]
                
        
        def helperr(i):
            if i == n:
                return float('-inf')
            if i not in dpr:
                dpr[i] = helperr(i+1) if height[i] < helperr(i+1) else height[i]
            return dpr[i]
        
        helperl(n-1)
        helperr(0)
        
        water = 0
        for i in range(n):
            water += min(dpl[i],dpr[i]) - height[i]
        return water