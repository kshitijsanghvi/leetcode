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
        right = [math.inf for i in range(n)]
        if seats[-1] == 1:
            right[-1] = 0
        for i in range(n-2,-1,-1):
            if seats[i] == 1:
                right[i] = 0
            else:
                right[i] = 1 + right[i+1]
        # print(left)
        # print(right)
        return max([min(i[0],i[1]) for i in zip(left,right)])