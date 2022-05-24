class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cl = []
        ans = []
        def helper(i,target):
            if i == len(candidates):
                if target == 0:
                    ans.append(cl[:])
                return 
            
            if target < 0:
                return 
            
            helper(i+1,target)
            cl.append(candidates[i])
            helper(i,target - candidates[i])
            cl.pop()
            
        helper(0,target)
        return ans