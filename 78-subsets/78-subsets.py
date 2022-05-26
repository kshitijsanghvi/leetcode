class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        current subset:
        Choice at each point select or not to select
        """
        ans = []
        cs = []
        def generate_subsets(i):
            if i == len(nums):
                ans.append(cs[:])
            
            else:
                generate_subsets(i+1)
                cs.append(nums[i])
                generate_subsets(i+1)
                cs.pop()
                
        generate_subsets(0)
        return ans