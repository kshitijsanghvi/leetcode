class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        zeros = {}
        for i,j in mines:
            zeros[i,j] = 1
            
        dp = [[0 if (i,j) in zeros else 1 for j in range(n)] for i in range(n)]
        dp_l = copy.deepcopy(dp)
        dp_r = copy.deepcopy(dp)
        dp_t = copy.deepcopy(dp)
        dp_b = copy.deepcopy(dp)
        
        for i in range(n):
            for j in range(1,n):
                dp_l[i][j] = (dp_l[i][j-1] + 1) if dp[i][j] == 1 else 0 
                dp_t[j][i] = (dp_t[j-1][i] + 1) if dp[j][i] == 1 else 0
                        
        for i in range(n):
            for j in range(n-2,-1,-1):
                dp_r[i][j] = (dp_r[i][j+1] + 1) if dp[i][j] == 1 else 0 
                dp_b[j][i] = (dp_b[j+1][i] + 1) if dp[j][i] == 1 else 0
        
        ans = 0
        
        for i in range(n):
            for j in range(n):
                if dp[i][j]:
                    ans = max(ans,min(dp_l[i][j],dp_r[i][j],dp_t[i][j],dp_b[i][j]))
        print(dp)
        return ans