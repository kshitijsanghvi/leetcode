class Solution:
    def canJump(self, nums: List[int]) -> bool:

        
        max_distance = 0
        current  = 0
        
        for i,v in enumerate(nums):
            if i <= max_distance:
                current+=v
                max_distance = max(max_distance, i + v)
            else:
                return False
            
        return True