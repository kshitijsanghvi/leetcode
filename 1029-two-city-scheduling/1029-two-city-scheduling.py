class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs_diff = [[i[0]-i[1],idx] for idx,i in enumerate(costs)]
        costs_diff.sort(reverse=True)
        ans = 0
        for i in range(len(costs)//2):
            ans+=costs[costs_diff[i][1]][1]
        
        for i in range(len(costs)//2,len(costs)):
            ans+=costs[costs_diff[i][1]][0]
        
        return ans