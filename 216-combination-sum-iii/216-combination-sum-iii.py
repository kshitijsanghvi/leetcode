class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        seen = [0] * 10
        current_ans = [0]
        ans = []
        def helper(current_sum, current_count):
            if current_count == k:
                if current_sum == n:
                    ans.append(current_ans[1:])
                return
            else:
                
                for i in range(current_ans[-1]+1,10):
                    if not seen[i]:
                        seen[i] = 1
                        current_ans.append(i)
                        helper(current_sum + i, current_count + 1)
                        seen[i] = 0
                        current_ans.pop()

        helper(0,0)
        return ans