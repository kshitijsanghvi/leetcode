class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        dp = {}
        ans = []
        size = defaultdict(int)
        def union(cx,cy,nx,ny):
            copy_x,copy_y = nx,ny
            while dp[nx,ny]!=(nx,ny):
                (nx,ny) = dp[nx,ny]
            dp[nx,ny] = (cx,cy)
            dp[copy_x,copy_y] = (cx,cy)
            size[cx,cy] = size[nx,ny] + 1
            del(size[nx,ny])
            
        def collapse():
            # s = set()
            # for (cx,cy) in dp:
            #     copy_x,copy_y = cx,cy
            #     while dp[cx,cy]!=(cx,cy):
            #         (cx,cy) = dp[cx,cy]
            #     s.add((cx,cy))
            #     dp[copy_x,copy_y] = (cx,cy)
            # ans.append(len(s))
            # count =0 
            # for (cx,cy) in dp:
            #     if dp[cx,cy] == (cx,cy):
            #         count+=1
            ans.append(len(size))
        for cx,cy in positions:
            dp[cx,cy] = (cx,cy)
            
            l = (cx,cy-1)
            r = (cx, cy +1)
            t = (cx-1,cy)
            b = (cx+1,cy)

            for nx,ny in [l,r,t,b]:
                if 0<=nx<m and 0<=ny<n and (nx,ny) in dp:
                    union(cx,cy,nx,ny)
            if (cx,cy) not in size:
                size[cx,cy] = 1
            collapse()

        return ans