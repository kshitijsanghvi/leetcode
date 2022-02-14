class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        dp = {}
        def helper(i,n1,n2):
            if i  == len(costs):
                if n1 != n2:
                    return math.inf
                else:
                    return 0
                
            if (i,n1,n2) not in dp:
                dp[i,n1,n2] = min(costs[i][0] + helper(i+1,n1-1,n2),costs[i][1] + helper(i+1,n1,n2-1))
            return dp[i,n1,n2]
        
        return helper(0,len(costs)//2,len(costs)//2)