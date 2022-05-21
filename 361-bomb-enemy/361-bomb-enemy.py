class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m ,n = len(grid), len(grid[0])
        ans = 0
        row = {}
        col = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    cans = 0
                    if (i,j) not in row:
                        count = 0
                        left = j - 1
                        while left >= 0 and grid[i][left] != "W":
                            if grid[i][left] == "E":
                                count += 1
                            left -= 1

                        right = j + 1
                        while right < n and grid[i][right] != "W":
                            if grid[i][right] == "E":
                                count += 1
                            right += 1
                        for jj in range(left+1,right):
                            row[i,jj] = count
                    
                    cans += row[i,j]
                        
                    if (i,j) not in col:
                        count = 0
                        top = i - 1
                        while top >= 0 and grid[top][j] != "W":
                            if grid[top][j] == "E":
                                count += 1
                            top -= 1

                        bottom = i + 1
                        while bottom < m and grid[bottom][j] != "W":
                            if grid[bottom][j] == "E":
                                count += 1
                            bottom += 1
                        for ii in range(top+1,bottom):
                            col[ii,j] = count
                    
                    cans += col[i,j]
                    ans = max(ans,cans)
                    
        return ans
                    