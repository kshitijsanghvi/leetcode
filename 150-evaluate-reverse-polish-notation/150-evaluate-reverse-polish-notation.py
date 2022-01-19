class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if t not in ['+','-','*','/']:
                stack.append(int(t))
            else:
                a = stack.pop()
                b = stack.pop()
                if t == '+':
                    stack.append(b + a)
                elif t == '-':
                    stack.append(b - a)
                elif t == '*':
                    stack.append(b * a)
                elif t == '/':
                    if a * b > 0:
                        stack.append(b//a)
                    else:
                        stack.append(abs(b)//abs(a)*-1)
                    
                
        return stack.pop()