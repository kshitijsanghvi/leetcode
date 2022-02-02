class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        def helper(s,k):
            if k == 4:
                if s:
                    return [False, []]
                else:
                    return [True,[""]]
            
            if not s:
                return [False,[]]
            
            else:
                
                ans = []
                #len1
                if len(s) >= 1:
                    pre = s[:1]
                    suf = s[1:]
                    a = helper(suf,k+1)
                    if a[0]:
                        for rem in a[1]:
                            ans.append(pre+'.'+rem)
                
                #len2
                if len(s) >= 2:
                    pre = s[:2]
                    suf = s[2:]
                    if pre[0]!='0':
                        a = helper(suf,k+1)
                        if a[0]:
                            for rem in a[1]:
                                ans.append(pre+'.'+rem)
                
                #len3
                if len(s) >= 3:
                    pre = s[:3]
                    suf = s[3:]
                    # No need to check second zero as first is not zero ---> meaning of leading zero
                    if pre[0]!='0'  and int(pre) <= 255:
                        a = helper(suf,k+1)
                        if a[0]:
                            for rem in a[1]:
                                ans.append(pre+'.'+rem)
                                
            return [True,ans] if len(ans)>0 else [False,[]]
        
        return [a[:-1] for a in helper(s,0)[1]]
