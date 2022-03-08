class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = [[0,heights[0]]]
        ans = 0
        for i in range(n):
            if heights[i] > stack[-1][1]:
                stack.append([i,heights[i]])
            else:
                last_i = 0
                while stack and stack[-1][1] >= heights[i]:
                    last_i, last_height = stack.pop()
                    ans = max(ans,last_height * (i - last_i))
                stack.append([last_i,heights[i]])
                
        while stack:
            ans = max(ans,(n - stack[-1][0]) * stack[-1][1])
            stack.pop()
            
        return ans