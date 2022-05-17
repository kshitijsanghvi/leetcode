class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n-3):
            if i == 0 or nums[i] != nums[i-1]:
                for j in range(i+1,n-2):
                    if j == i + 1 or nums[j] != nums[j-1]:
                        l = j + 1
                        r = n - 1
                        while l < r:
                            if nums[l] + nums[r] + nums[j] + nums[i] > target:
                                r -= 1
                            elif nums[l] + nums[r] + nums[j] + nums[i] < target:
                                l +=1
                            else:
                                ans.append([nums[i], nums[j], nums[l], nums[r]])
                                l+=1
                                r -= 1
                                while l < r and nums[l] == nums[l-1]:
                                    l+=1
                                    
                                    
                                    
        return ans