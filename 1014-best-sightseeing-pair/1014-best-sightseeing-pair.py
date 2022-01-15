class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        left = values[0] - 1
        result = float('-inf')
        
        for i in range(1,len(values)):
            result = max(left + values[i],result)
            left = max(values[i],left) - 1
        return result
            
            
            