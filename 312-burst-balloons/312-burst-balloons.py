class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        Bursting last 
        
        Recurrence relation :
        
        """
        
        
        
        nums = [1] + nums + [1]
        n = len(nums)
        
        dp = [[0 for j in range(n)] for i in range(n)]
        for i in range(1,n-1):
            dp[i][i] = nums[i]
        
        for i in range(n-2,0,-1):
            for j in range(1, n - 1):
                dp[i][j] = max([0]+[dp[i][k-1] + nums[k]*nums[i - 1]*nums[j+1] + dp[k+1][j] for k in range(i,j+1)])
        return dp[1][n-2]
    
    

        
        