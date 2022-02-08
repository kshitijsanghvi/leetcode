class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_peak = math.inf
        max_value = -math.inf
        
        for i in prices:
            max_value = max(max_value,i - min_peak)
            min_peak = min(min_peak,i)
            
        return max_value if max_value > 0 else 0
            