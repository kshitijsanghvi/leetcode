class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        c = Counter(nums)
        nums = list(c.keys())
        
        nums.sort()
        n = len(nums)
        
        i = 0
        while i <= n-k:
            if c[nums[i]] != 0:
                for j in range(nums[i],nums[i]+k):
                    if j not in c or c[j] == 0:
                        return False
                    else:
                        c[j]-=1
                
            else:
                i+=1
        while i < n:
            if c[nums[i]]!= 0:
                return False
            i+=1
                
        return True
                    
        