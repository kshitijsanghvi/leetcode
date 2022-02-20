class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        n = len(bulbs)
        day = [-1]*(n+1)
        for i,v in enumerate(bulbs):
            day[v] = i+1
            
        start = 1
        end = start + k + 1
        ans = []
        while end < n+1:
            flag = True
            for j in range(start+1,end):
                if day[j] < day[start] or day[j] < day[end]:
                    end = j
                    flag = False
                    break
            if flag:
                ans.append(max(day[start],day[end]))
            start = end
            end = start + k + 1
            
        return min(ans) if ans else -1