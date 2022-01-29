class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums
        
        min_v , min_i = float('inf'), -1
        
        for i,v in enumerate(nums[:n-k+1]):
            if v < min_v:
                min_v = v
                min_i = i
        
        solution = [min_v]
        idx = min_i
        if k == 1:
            return solution
        nums1 = [[v,i+idx+1] for i,v in enumerate(nums[idx+1:n-k+2])]
        r = n-k+2
        heapq.heapify(nums1)
        
        prev_index = -1
        k -= 1
        while k > 0:
            nn = heapq.heappop(nums1)
            if prev_index > nn[1]:
                continue
            else:
                prev_index = nn[1]
                solution.append(nn[0])
                k -= 1
                if r < n:
                    heapq.heappush(nums1,[nums[r],r])
                    r+=1
        
        return solution