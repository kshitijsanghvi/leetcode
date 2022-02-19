class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """
        Approach remove the dominoes with the same number and record the number
        -> Removed dominoes can only have 1 value
        -> if they have different return - 1
        -> Check if we can make a combination
        -> dp
        """
        flag = 1
        n = len(tops)
        removed_value = None
        temp_tops = []
        temp_bottoms = []
        d = defaultdict(int)
        for i in range(n):
            if tops[i] != bottoms[i]:
                temp_tops.append(tops[i])
                d[tops[i]]+=1
                d[bottoms[i]]+=1
                temp_bottoms.append(bottoms[i])
            else:
                if flag:
                    removed_value = tops[i]
                    flag = 0
                else:
                    if removed_value != tops[i]:
                        return -1
                    
        tops = temp_tops
        bottoms = temp_bottoms
        
        n = len(tops)
        if not d:
            return 0
        if max(d.values()) < n:
            return -1
        
        a = 0
        a1 = 0
        b = 0
        b1 = 0
        
        if removed_value:
            target = removed_value
            for i in range(n):
                if tops[i] != target and bottoms[i]!= target:
                    a = math.inf
                else:
                    if bottoms[i] == target:
                        a+=1
            target = removed_value
            for i in range(n):
                if bottoms[i] != target and tops[i] != target:
                    a1 = math.inf
                elif tops[i] == target:
                    a1+=1
            return min(a,a1) if min(a,a1)!= math.inf else -1
    
        
        target = tops[0]
        for i in range(n):
            if tops[i] != target:
                a+=1
        target = bottoms[0]
        for i in range(n):
            if tops[i] != target:
                a1+=1
        
        target = bottoms[0]
        for i in range(n):
            if bottoms[i] != target:
                b+=1
        
        target = tops[0]
        for i in range(n):
            if bottoms[i] != target:
                b1+=1
        # print(a,b,a1,b1)
        return min(a,b,a1,b1)
                
            