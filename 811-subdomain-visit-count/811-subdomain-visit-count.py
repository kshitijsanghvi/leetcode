class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = defaultdict(int)
        for q in cpdomains:
            l = q.split(' ')
            count = int(l[0])
            l = l[1].split('.')
            for i in range(1,len(l)+1):
                d['.'.join(l[-i:])] += count               
                
        ans = [str(d[i])+' '+str(i) for i in d]
        
        return ans