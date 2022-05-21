class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        
        dp = {}
        
        def helper(pile_index, k):
            if pile_index == n or k <= 0:
                return 0
            if (pile_index,k) not in dp:
                temp = helper(pile_index + 1, k)
                sum = 0
                for i in range(1,min(k,len(piles[pile_index]))+1):
                    # No need to comopute prefix sum as it is overwork
                    sum += piles[pile_index][i-1]
                    temp = max(temp,sum + helper(pile_index+1,k-i))
                dp[pile_index,k] = temp
            return dp[pile_index,k]
        
        return helper(0,k)
                
                