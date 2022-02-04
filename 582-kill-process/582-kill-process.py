class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:

        p = {}
        for i,v in enumerate(ppid):
            p[pid[i]] = v
            
        if p[kill] == 0:
            return pid
        ans = []
        p[kill]=kill
        for i in pid:
            copy = i
            while p[i]!=kill and p[i]!=0:
                i = p[i]
                
            if p[i] == kill:
                ans.append(copy)
                
        return ans