class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        d = Counter(tasks)
        
        max_v, max_key = 0,0
        
        for k,v in d.items():
            if max_v < v:
                max_v = v
                max_key = k
                
        intervals = max_v - 1
        ans = max_v
        remaining = intervals * n
        ans = max_v + remaining
        del(d[max_key])
        
        for v in sorted(d.values()):
            if v > intervals:
                if remaining - intervals >= 0:
                    remaining = remaining - intervals
                    ans+=1
                else:
                    ans+= v - remaining
                    remaining  = 0
            else:
                if remaining - v >= 0:
                    remaining = remaining - v
                else:
                    ans+=v - remaining
                    remaining  = 0
        return ans