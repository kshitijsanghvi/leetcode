class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        left = [math.inf for i in range(n)]
        if seats[0] == 1:
            left[0] = 0
        for i in range(1,n):
            if seats[i] == 1:
                left[i] = 0
            else:
                left[i] = left[i-1]+1
        if seats[-1] == 1:
            left[-1] = 0
        prev = left[-1]
        for i in range(n-2,-1,-1):
            if seats[i] == 1:
                left[i] = 0
                prev = 0
            else:
                prev+=1
                left[i] = min(prev,left[i])
                
        # print(left)
        # print(right)
        return max(left)