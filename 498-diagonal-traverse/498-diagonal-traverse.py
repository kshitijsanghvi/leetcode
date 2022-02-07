class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        m, n = len(mat), len(mat[0])
        d = 0
        ans = []
        cx, cy = 0, 0
        while len(ans) < m * n:

            if 0 <= cx < m and 0 <= cy < n:
                ans.append(mat[cx][cy])
                if d == 0:
                    cx -= 1
                    cy += 1
                else:
                    cx += 1
                    cy -= 1
                continue

            if cx < 0 and cy >= n:
                d = 1
                cx += 2
                cy -= 1
                continue

            if cx >= m and cy < 0:
                d = 0
                cx -= 1
                cy += 2
                continue

            if cx < 0:
                d = 1
                cx += 1
                continue

            if cx >= m:
                d = 0
                cx -= 1
                cy += 2
                continue

            if cy < 0:
                d = 0
                cy += 1
                continue
            if cy >= n:
                d = 1
                cx += 2
                cy -= 1
                continue
        return ans

