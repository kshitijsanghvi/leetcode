class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        h = []
        n = len(nums)
        h = [[nums[0],1]]
        
        for i in range(1,n):
            if h:
                cl = heapq.heappop(h)
                if cl[0] + 1== nums[i]:
                    cl[0]+=1
                    cl[1]+=1

                    if cl[1] < k:
                        heapq.heappush(h,cl)

                elif cl[0] == nums[i]:
                    heapq.heappush(h,cl)
                    heapq.heappush(h,[nums[i],1])

                else:
                    return False
            else:
                heapq.heappush(h,[nums[i],1])
        if h:
            return False
        return True