class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = [i for i in range(1,n+1)]
        
        def helper(n,k,arr):
            if n == 0:
                return ""
            if k == 0:
                s = ""
                for i in arr:
                    s = s + str(i)

                return s
            
            d = k//math.factorial(n-1)
            r = k % math.factorial(n-1)
            return str(arr.pop(d)) + helper(n-1,r,arr)
        
        return helper(n,k-1,arr)