class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = set()
        def helper(n,k,contains):
            nonlocal ans
            # base case 
            if n == 0 and k == 0:
                # print(bin(contains))
                
                current_ans = []
                for i in range(9):
                    ele = 1 << i
                    if ele & contains != 0:
                        current_ans.append(i+1)
                current_ans.sort()
                ans.add(tuple(current_ans))
            
            elif k == 0 or n < 0:
                return
            
            #recurrence relation 
            for i in range(9):
                ele = 1 << i
                if contains & ele == 0:
                    # print(bin(contains), bin(contains | ele) )
                    helper(n - i-1, k - 1,contains | ele)
                    
        helper(n,k,0)
        return ans