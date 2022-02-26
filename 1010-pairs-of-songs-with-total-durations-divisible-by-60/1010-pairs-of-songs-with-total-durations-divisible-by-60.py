class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d = defaultdict(int)
        ans = 0
        for i in time:
            r = (60 - (i % 60))%60
            ans += d[r]
            d[i % 60]+=1    
        return ans