class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        d = n - 1
        ans = n
        dup = [1]
        for i in range(1,n):
            if nums[i] == nums[i-1]:
                dup.append(dup[-1])
            else:
                dup.append(dup[-1]+1)
                
        for i in range(n):
            right_limit = nums[i] + d
            idx = bisect.bisect_right(nums,right_limit)
            flip_right = n - idx
            # i to idx -1 
            duplicates = (idx -i) - (dup[idx-1] - dup[i] + 1)
            left = i
            ans = min(ans,flip_right + duplicates + left)
        return ans