class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        n = len(nums)
        
        for i in range(k):
            heapq.heappush(heap,nums[i])

        for i in range(k,n):
            heapq.heappush(heap,nums[i])
            heapq.heappop(heap)
            
        return heap[0]