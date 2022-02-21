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
            for l in range(i+1,n-1):
                max_v = nums[i] + nums[l] - 1
                right = bisect.bisect_right(nums,max_v,lo=l+1)
                ans+= right - 1 - l 
          
        return ans
                    
                