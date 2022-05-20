class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x : x[1])
        n = len(pairs)
        ans = 1
        min_v = pairs[0][1]
        for i in range(n-1):
            if min_v < pairs[i+1][0]:
                min_v = pairs[i+1][1]
                ans += 1
            
        return ans
        