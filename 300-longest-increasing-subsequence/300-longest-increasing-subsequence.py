class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subs = []
        for i in nums:
            if not subs:
                subs.append(i)
            else:
                if i > subs[-1]:
                    subs.append(i)
                else:
                    idx = bisect.bisect_left(subs,i)
                    subs[idx] = i
        return len(subs)