class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ans = float('-inf')
        n = len(cardPoints)
        
        sum1 = [0]
        for i in range(k):
            sum1.append(sum1[-1]+cardPoints[i])
        sum2 = [0]
        for j in range(n-1,n-k-1,-1):
            sum2.append(sum2[-1]+cardPoints[j])
            
        sum2 = sum2[::-1]
        
        return max([i[0]+i[1] for i in zip(sum1,sum2)])