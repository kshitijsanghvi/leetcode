class TrieNode:
    def __init__(self):
        self.val = False
        self.d = defaultdict(TrieNode)
    
    
    def add(self,node,word,i):
        if i == len(word):
            node.val = True
        else:
            self.add(node.d[word[i]],word,i+1)
            
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()
        
        for w in words:
            root.add(root,w,0)
            
        m,n = len(board), len(board[0])
        
        def compute(i,j,root,v,word):
            if root.val:
                ans.add(word)
            
            l = (i,j-1)
            r = (i,j+1)
            t = (i-1,j)
            b = (i+1,j)
            
            for ni,nj in [l,r,t,b]:
                if 0 <= ni < m and 0<=nj<n and v[ni,nj] == 0 and board[ni][nj] in root.d:
                    v[ni,nj] = 1
                    compute(ni,nj,root.d[board[ni][nj]],v,word + board[ni][nj])
            v[i,j] = 0
            
        ans = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] in root.d:
                    v = defaultdict(int)
                    v[i,j] = 1
                    compute(i,j,root.d[board[i][j]],v,board[i][j])
                
        return list(ans)