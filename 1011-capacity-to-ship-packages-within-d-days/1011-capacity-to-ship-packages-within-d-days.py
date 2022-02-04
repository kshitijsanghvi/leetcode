class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        
        
        def find(limit):
            count = 1
            csum = 0
            for i in weights:
                if csum + i > limit:
                    csum = i
                    count+=1
                else:
                    csum+=i
            return count
        
        while l < r:
            mid = l + (r- l )//2
            
            val = find(mid)
            if val <= days:
                r = mid
            else:
                l = mid + 1
                    
                    
        return l