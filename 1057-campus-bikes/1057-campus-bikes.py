class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        def compute_distance(p1,p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        d = defaultdict(list)
        max_d = 0
        min_d = 2*10**3 -1
        for i,w in enumerate(workers):
            for j,b in enumerate(bikes):
                dist = compute_distance(w,b)
                min_d = min(min_d, dist)
                max_d = max(max_d, dist)
                d[dist].append([i,j])
        nw = len(workers)
        nb = len(bikes)
        
        avail = [True]*nb
        assigned = [-1] * nw
        count = 0
        curr = min_d

        while count < nw:
            if count == nw:
                break
            for w,b in d[curr]:
                if count == nw:
                    break
                if assigned[w] == -1 and avail[b]:
                    avail[b] = False
                    assigned[w] = b
                    count+=1
            curr+=1
        return assigned