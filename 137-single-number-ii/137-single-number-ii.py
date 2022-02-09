class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n3 = ~0
        n31 = 0
        n32 = 0
        
        for i in nums:
            cwn3 = i & n3
            cwn31 = i & n31
            cwn32 = i & n32
            
            n3 = n3 | cwn32
            n31 = n31 | cwn3
            n32 = n32 | cwn31
            
            n3 = n3 & ~cwn3
            n31 = n31 & ~cwn31
            n32 = n32 & ~cwn32
        
        return n31