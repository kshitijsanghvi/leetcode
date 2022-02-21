class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        def isValid(a,b,c):
            if a + b > c and a + c > b and b + c > a:
                return True
            return False        
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n-2):
            l = i + 1
            r = l + 1
            while l < n-1:
                while r < n and nums[i] + nums[l] > nums[r]:
                    ans+= r - l
                    r +=1
                l +=1
                if l == r:
                    r = l + 1
                
                    
        return ans