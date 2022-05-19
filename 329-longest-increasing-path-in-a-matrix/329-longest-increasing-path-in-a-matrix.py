class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        visited = {}
        computed = {}
        max_path = -math.inf
        
        m, n = len(matrix), len(matrix[0])
        
        
        def dfs(i,j):
            visited[i,j] = 1
            l = [i,j - 1]
            r = [i,j + 1]
            t = [i -1, j]
            b = [i + 1,j]
            current_length = 0
            for ni,nj in [l,r,t,b]:
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    if (ni,nj) in computed:
                        current_length = max(current_length, computed[ni,nj])
                    elif (ni,nj) not in visited:
                        current_length = max(current_length, dfs(ni,nj))
            computed[i,j] = 1 + current_length
            return 1 + current_length
            
        for i in range(m):
            for j in range(n):
                if (m,n) not in visited:
                    max_path = max(max_path,dfs(i,j))
                    
        return max_path