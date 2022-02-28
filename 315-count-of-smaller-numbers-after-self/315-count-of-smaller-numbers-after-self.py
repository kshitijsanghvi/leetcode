class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        nums = [[v,i] for i,v in enumerate(nums)]
        def merge(l,r):
            if l == r:
                return [nums[l]]
            
            mid = l + (r-l)//2
            left = merge(l,mid)
            right = merge(mid+1,r)
            jumps = 0
            l1 = 0
            l2 = 0
            ans = []
            while l1 < len(left) and l2 < len(right):
                if left[l1][0] > right[l2][0]:
                    ans.append(right[l2])
                    jumps+=1
                    l2 += 1
                else:
                    d[left[l1][1]]+=jumps
                    ans.append(left[l1])
                    l1+=1
                    
            while l2 < len(right):
                ans.append(right[l2])
                jumps+=1
                l2 += 1

            while l1 < len(left):
                d[left[l1][1]]+=jumps
                ans.append(left[l1])
                l1+=1
            return ans
        
        merge(0,len(nums)-1)
        return [d[i] for i in range(len(nums))]
                