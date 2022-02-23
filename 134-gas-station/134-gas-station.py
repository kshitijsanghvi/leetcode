class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        min_r = [-cost[i]+gas[i] for i in range(n)]
        if sum(min_r) < 0:
            return - 1
        
        csum = 0
        ci = 0
        
        for i,v in enumerate(min_r):
            csum += v
            if csum < 0:
                csum = 0
                ci = i + 1
        return ci