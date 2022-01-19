class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        s =list(s)
        for i,c in enumerate(s):
            if c == '(':
                stack.append(i)
            if c ==')':
                l = stack.pop()
                s[l+1:i] = s[l+1:i][::-1]
        
        return ''.join([i for i in s if i !='(' and i != ')'])            