class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 == 1:
            return []
        changed.sort()
        d = defaultdict(int)
        ans = []
        for i in changed:
            if i%2 == 0 and i//2 in d:
                ans.append(i//2)
                if d[i//2] == 1:
                    del(d[i//2])
                else:
                    d[i//2]-=1
            else:
                d[i] +=1
        if len(ans) == n/2:
            return ans
        else:
            return []