class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        for i,v in enumerate(nums):
            d[v] = i
            
        visited = {}
        ans = 0
        for i,v in enumerate(nums):
            if v not in visited:
                current_len = 1
                
                cv = v
                while cv + 1 in d:
                    if (cv  + 1) in visited:
                        current_len += visited[cv + 1]
                        break
                    else:
                        current_len += 1
                        visited[cv + 1] = current_len
                        cv += 1
                visited[v] = current_len
                ans = max(ans,current_len)

        return ans