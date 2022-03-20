class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        left_max = right_max = -math.inf
        if left:
            left_max = max(left)
        if right:
            right_max = n - min(right)
            
        return max(left_max,right_max)