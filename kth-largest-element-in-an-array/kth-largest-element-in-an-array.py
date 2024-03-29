class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        h = []
        i = 0
        while len(h) < k:
            heapq.heappush(h,nums[i])
            i+=1
            
        while i < len(nums):
            heapq.heappushpop(h,nums[i])
            i+=1
            
        return h[0]