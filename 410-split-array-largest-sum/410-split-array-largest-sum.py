class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        
        
        l = max(nums)
        r = sum(nums)
        
        
        def check(target):
            csum = 0
            max_sum = float('-inf')
            count = 1
            
            for i in nums:
                if csum + i <= target:
                    csum += i
                    
                else:
                    csum = i
                    count+=1
                max_sum = max(max_sum,csum)
            return True if max_sum <= target and count <= m else False
                
                
        while l < r:
            mid = l + (r-l)//2
            if check(mid):
                r = mid
            else:
                l = mid + 1
                
        return l 