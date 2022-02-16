class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Appr
        """
        n = len(isConnected)
        visited = [None for i in range(n)]
        
        ans = 0
        for i in range(n):
            if visited[i] == None:
                ans+=1
                visited[i] = 1
                q = [i]
                while q:
                    cn = q.pop(0)
                    for nn,v in enumerate(isConnected[cn]):
                        if v == 1 and visited[nn] == None:
                            visited[nn] = 1
                            q.append(nn)
        return ans