class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m,n = len(mat),len(mat[0])
        d = defaultdict(list)
        for i in range(m):
            for j in range(n):
                d[i+j].append(mat[i][j])
        
        ans = []
        for i in d:
            if i %2 == 1:
                ans.extend(d[i])
            else:
                ans.extend(d[i][::-1])
        return ans
            