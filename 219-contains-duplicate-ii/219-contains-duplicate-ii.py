class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = defaultdict(int)
        
        for i,v in enumerate(nums):
            if v in d:
                if i - d[v] <= k:
                    return True

            d[v] = i
