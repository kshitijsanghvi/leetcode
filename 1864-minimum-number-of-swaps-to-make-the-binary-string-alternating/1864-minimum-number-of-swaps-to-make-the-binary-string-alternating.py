class Solution:
    def minSwaps(self, s: str) -> int:
        if s == '1' or s == '0':
            return 0
        
        d = Counter(s)
        if '1' not in d or '0' not in d:
            return -1
        
        val = d.values()
        mi = min(val)
        ma = max(val)
        
        dif = ma - mi
        
        if dif> 1:
            return -1
        
        
        if dif == 1:
            start = '1'
            if d['0'] > d['1']:
                start = '0'
            swap = 0
            for i in s[0::2]:
                if i != start:
                    swap+=1
            return swap
        
        ans1 = 0
        start = '0'
        for i in s[0::2]:
            if i != start:
                ans1+=1
                
        ans2 =0
        start = '1'
        for i in s[0::2]:
            if i!=start:
                ans2+=1
        return min(ans1,ans2)
        