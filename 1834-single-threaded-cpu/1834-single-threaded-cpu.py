class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
    
        
        h = []
        
        i = 0
        n = len(tasks)
        ans = []
        
        for i in range(n):
            tasks[i].append(i)
        tasks.sort()
        i = 0
        start = tasks[0][0]
        while True:
            while i < n and tasks[i][0] <= start:
                heapq.heappush(h,(tasks[i][1],tasks[i][2]))
                i+= 1
                
            if not h:
                if i == n:
                    return ans
                else:
                    start = tasks[i][0]
                    continue
                    
            ct = heapq.heappop(h)
            ans.append(ct[1])
            start += ct[0]
            