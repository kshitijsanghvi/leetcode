class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return 0
        next_jump = 0
        current_jump = 0
        ans = 0
        for i in range(n):
            if current_jump < i:
                ans+=1
                current_jump = next_jump
            next_jump = max(next_jump,i + nums[i])
        return ans