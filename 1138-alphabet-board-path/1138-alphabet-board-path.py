class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        m = 5
        n = 5
        board = {}
        count = 0
        for i in range(m):
            for j in range(n):
                board[chr(count + ord('a'))] = (i,j)
                count += 1
        board['z'] = (5,0)
        start = (0,0)
        ans = ""
        for c in target:
            t = board[c]
            
            dx = t[0] - start[0]
            dy = t[1] - start[1]

            if t == start:
                ans+='!'
              
            #1. left and top

            elif dx < 0 and dy < 0:
                ans+= 'L'*abs(dy)
                ans+= 'U'*abs(dx)
                ans+='!'
            

            #2. top and right:
            elif dx < 0 and dy >= 0:
                ans+='U'*abs(dx)
                ans+='R'*dy
                ans+='!'
           

            #3 left and down
            elif dx >= 0 and dy < 0:
                ans += 'L'*abs(dy)
                ans += 'D'*dx
                ans +='!'
              

            #4 right and bottom:
            elif dx>= 0 and dy>=0:
                ans+='R'*dy
                ans+='D'*dx
                ans+='!'
           
            
            start = t
        return ans
                        
                