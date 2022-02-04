class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        
        dp = {}
        @lru_cache(None)
        def helper(i,expire):
            if i >= len(days):
                return 0
            
            
            if days[i] <= expire:
                
                return helper(i+1,expire)
            
            else:
                return min(costs[0] + helper(i+1,days[i] + 1 - 1),costs[1] + helper(i+1,days[i] + 7 - 1),costs[2] + helper(i+1,days[i] + 30 - 1))
            
        return helper(0,0)