class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        
        l = 0
        r = n - 1
        ans = 0
        while l < r:
            ans = max(ans,min(height[l],height[r])*(r - l))
            if height[l] > height[r]:
                r -=1
            else:
                l+=1
        return ans