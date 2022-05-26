class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x : x[1], reverse=True)
        envelopes.sort(key = lambda x : x[0])
        slow = 0
        n = len(envelopes)
        for fast in range(1,n):
            if envelopes[fast][1] > envelopes[slow][1]:
                slow += 1
                envelopes[slow] = envelopes[fast]
            else:
                i = bisect.bisect_left(envelopes, envelopes[fast][1], key = lambda x : x[1], hi = slow + 1)
                envelopes[i] = envelopes[fast]
        return slow + 1