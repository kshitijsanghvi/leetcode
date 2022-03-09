class Solution:
    def compress(self, chars: List[str]) -> int:
        np = 0
        op = 0
        
        while np < len(chars):
            cc = chars[np]
            c = 0
            
            while np < len(chars) and chars[np] == cc:
                np+=1
                c +=1
                
            chars[op] = cc
            op+=1
            if c > 1:
                for ccc in str(c):
                    chars[op] = ccc
                    op+=1
        return op
            