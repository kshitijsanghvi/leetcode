class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        '''
        3 sum closest
        min (|target - (n1 + n2 + n3)|)
        Ex: [-1,2,1,-4]
        [-4,-1,1,2]
        #1 = -4 + -1 + 1 = -4 => -3
        #2 = -4, -1 , 2 => -2
        #3 = -4, 1, 2 => -1 => -2
        #4 = -1 1 2 => 2 => -1
        '''
        d = math.inf
        nums.sort()
        n = len(nums)
        ans = math.inf
        for i in range(n-2):
            for j in range(i+1,n-1):
                find = target - nums[i] - nums[j]
                idx = bisect.bisect_left(nums,find,lo=j+1)
                
                if idx < n and nums[idx] == find:
                    return target
                
                if idx != n:
                    if d > abs(target - (nums[i] + nums[j] + nums[idx])):
                        ans = (nums[i] + nums[j] + nums[idx])
                        d = abs(target - (nums[i] + nums[j] + nums[idx]))
                    
                    
                if idx != 0 and idx - 1 > j: # Important Check!!!!!!!!!!!!!!!!!!!!
                    if d > abs(target - (nums[i] + nums[j] + nums[idx-1])):
                        ans = (nums[i] + nums[j] + nums[idx-1])
                        d = abs(target - (nums[i] + nums[j] + nums[idx-1]))

                # print(nums[i],nums[j],idx,d,ans)
        return ans
                        