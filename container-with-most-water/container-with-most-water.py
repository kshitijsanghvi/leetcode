class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = -math.inf
        l = 0
        r = len(height) - 1
        while l < r:
            ans = max(ans,(r - l) * min(height[l],height[r]))
            if height[l] > height[r]:
                r -= 1
            else:
                l+=1
        return ans