class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow1 = slow2 = 0
        fast = nums[nums[slow1]]
        slow1 = nums[slow1]
        while slow1 != fast:
            slow1 = nums[slow1]
            fast = nums[nums[fast]]
            
        while slow2 != slow1:
            slow2 = nums[slow2]
            slow1 = nums[slow1]
        
        return slow1
        