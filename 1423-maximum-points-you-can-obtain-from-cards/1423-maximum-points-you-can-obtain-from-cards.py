class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ans = float('-inf')
        n = len(cardPoints)
        
        sum1 = 0
        for i in range(k):
            sum1+=cardPoints[i]
        
        ans = sum1
        for j in range(n-1,n-k-1,-1):
            sum1+= cardPoints[j]
            sum1 -= cardPoints[k - n + j]
            ans = max(ans,sum1)
            
        return ans