class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_1 = math.inf
        min_2 = math.inf
        
        for i in nums:
            if i <= min_1:
                min_1 = i
            elif i <= min_2:
                min_2 = i
            else:
                return True
        return False