class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        v = {}
        sx = 0
        sy = 0
        m = len(matrix)
        n = len(matrix[0])
        ans = []
        prev = None
        while prev != len(ans):
            prev = len(ans)
            # go rright
            while (sx, sy) not in v and sy < n:
                v[sx, sy] = 1
                ans.append(matrix[sx][sy])
                sy += 1
            sy -= 1
            sx += 1

            # go down
            while (sx, sy) not in v and sx < m:
                v[sx, sy] = 1
                ans.append(matrix[sx][sy])
                sx += 1
            sx -= 1
            sy -= 1

            # go left
            while (sx, sy) not in v and sy >= 0:
                v[sx, sy] = 1
                ans.append(matrix[sx][sy])
                sy -= 1
            sy += 1
            sx -= 1

            # go top
            while (sx, sy) not in v and sx >= 0:
                v[sx, sy] = 1
                ans.append(matrix[sx][sy])
                sx -= 1
            sx += 1
            sy += 1

        return ans