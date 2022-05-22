class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        val = image[sr][sc]
        q = deque()
        q.append([sr,sc])
        seen = set()
        seen.add((sr,sc))
        while q:
            ci,cj = q.popleft()
            image[ci][cj] = newColor
            
            l = [ci,cj-1]
            r = [ci,cj+1]
            t = [ci-1,cj]
            b = [ci+1,cj]
            
            
            for ni,nj in [l,r,t,b]:
                if 0 <= ni < len(image) and 0 <= nj < len(image[0]) and (ni,nj) not in seen and image[ni][nj] == val:
                    seen.add((ni,nj))
                    q.append([ni,nj])
        return image