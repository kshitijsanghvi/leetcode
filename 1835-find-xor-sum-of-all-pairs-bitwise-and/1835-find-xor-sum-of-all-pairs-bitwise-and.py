class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        acc1 = 0
        for i in arr1:
            acc1 = acc1 ^ i
        acc2 = 0
        for i in arr2:
            acc2 = acc2^i
            
        return acc1 & acc2