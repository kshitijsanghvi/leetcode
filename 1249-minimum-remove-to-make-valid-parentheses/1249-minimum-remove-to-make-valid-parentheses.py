class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        count = 0
        for i,v in enumerate(s):
            if v != '(' and v!=')':
                stack.append(v)
            else:
                if v == ')':
                    if count > 0:
                        count-=1
                        stack.append(v)
                elif v == '(':
                    count+=1
                    stack.append(v)
        
        ans = []
        while count > 0:
            cn = stack.pop()
            if cn == '(':
                count -=1
            else:
                ans = [cn] + ans
                
        return ''.join(stack + ans)
                