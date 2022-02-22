class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        
        l = 0
        r = 0
        ans = []
        while r < len(nums):
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)
            
            if r - l + 1> k:
                l+=1
                while dq[0] < l:
                    dq.popleft()
                    
            if r - l  + 1 == k:
                ans.append(nums[dq[0]])
            r+=1
            
        return ans