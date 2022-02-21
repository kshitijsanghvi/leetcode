class Solution:
    def numTrees(self, n: int) -> int:
        count = {}
        count[0] = 1
        count[1] = 1
        
        def counter(i):
            if i not in count:
                count[i] = sum([counter(j) * counter(i -j - 1) for j in range(0,i)])       
            return count[i]
        
        return counter(n)