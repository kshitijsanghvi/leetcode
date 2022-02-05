class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        for i in range(1,n+1):
            ans.append([i])
        if k == 1:
            return ans
        
        for i in range(2,k+1):
            new_ans = []
            for t in ans:
                for j in range(t[-1]+1,n+1):
                    new_ans.append(t + [j])
            ans = new_ans
            
        return ans