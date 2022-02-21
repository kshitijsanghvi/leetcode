class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = 1
        me = nums[0]
        for i in nums[1:]:
            if i != me:
                m -= 1
                if m == 0:
                    me = i
                    m = 1
            else:
                m+=1
        return me