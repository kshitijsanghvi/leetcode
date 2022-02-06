class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            return 0
        def numberless(k):
            d = Counter()
            l = 0
            res = 0
            for i in range(len(nums)):
                if d[nums[i]] == 0:
                    k-=1
                d[nums[i]]+=1
                while k < 0:
                    d[nums[l]]-=1
                    if d[nums[l]]==0:
                        k+=1
                    l+=1
                    
                res += i - l + 1
            return res
        
        return numberless(1) if k == 1 else numberless(k) - numberless(k-1)