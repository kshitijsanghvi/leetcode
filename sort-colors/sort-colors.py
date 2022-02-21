class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        Approach : The range of numbers is limited to [0,1,2]
        We can use counting sort
        Step 1 : Create a dictionary to count 
        Step 2 : iterate and update value
        
        """
        d = Counter(nums)
        start = 0
        while d[0]:
            nums[start] = 0
            start+=1
            d[0]-=1
        while d[1]:
            nums[start] = 1
            start+=1
            d[1]-=1
        while d[2]:
            nums[start] = 2
            start+=1
            d[2]-=1
            