class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        a = []
        r = maxWidth
        line = []
        current_line_length = 0
        for i, w in enumerate(words):
            n = len(w)
            if current_line_length + 1 + n > r:
                ans.append([line,current_line_length])
                line = [w]
                current_line_length =n
            else:
                
                if current_line_length != 0:
                    current_line_length += 1
                    w = " "+w
                current_line_length += n
                line.append(w)
                
        if current_line_length != 0 :
            ans.append([line,current_line_length])
        
        
        for (line,size) in ans[:-1]:
            if line:
                n = len(line)
                if n == 1:
                    a.append(line[0] + " "*(r - size))
                else:
                    s = r - size
                    i = 0
                    while s > 0:
                        line[i]=line[i] + " "
                        i = (i + 1)%(n-1)
                        s-=1
                    a.append(''.join(line))

        a.append("".join(ans[-1][0]) + " "*(r-ans[-1][1]))
            
        return a
                