class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        a  = grid[0]
        ia = [1-i for i in grid[0]]
        for i in grid[1:]:
            if i != a and i !=ia:
                return False
        return True
            