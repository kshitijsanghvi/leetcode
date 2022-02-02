class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        d = defaultdict(int)
        for i in clips:
            d[i[0]] = max(d[i[0]],i[1])
            
        clips = [[i,v] for i,v in d.items()]
        clips.sort()
        ans = 0
        p = 0
        n  = len(clips)
        print(clips)
        i = 0
        prev = 0
        while i < n:
            if p >= time:
                return ans
            maxi = float('-inf')
            while i < n and p >= clips[i][0]:
                maxi = max(maxi,clips[i][1])
                i+=1
                
            if i == prev:
                return -1
            prev = i
            p = maxi
            ans+=1
        return -1 if p < time else ans