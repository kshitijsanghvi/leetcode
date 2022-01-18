class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        
        for i in range(n):
            tasks[i].append(i)
            
        tasks.sort()
        
        ct = tasks[0][0]
        i = 0
        q = []
        processed = 0
        ans = []
        while True:
            while i < n and tasks[i][0]<= ct:
                bisect.insort_right(q,[tasks[i][1],tasks[i][2]],lo = processed) 
                i+=1
            
            if len(q) == processed:
                if i == n:
                    return ans
                else:
                    ct = tasks[i][0]
                    continue
            ans.append(q[processed][1])
            ct += q[processed][0]
            processed+=1