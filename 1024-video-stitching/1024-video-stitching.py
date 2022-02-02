class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        d = defaultdict(int)
        for i in clips:
            d[i[0]] = max(d[i[0]],i[1])
            
        clips = [[i,v] for i,v in d.items()]
        clips.sort()
        
        dp = {}
        n = len(clips)
        print(clips)
        def helper(i,s):
            if i == n:
                if s >= time:
                    return 0
                return float('inf')        
            
            if (i,s) not in dp:
                
                if clips[i][0]<= s < clips[i][1]:
                    dp[i,s] = min(1 + helper(i+1,clips[i][1]),helper(i+1,s))
                else:
                    dp[i,s] = helper(i+1,s)
            # print(i,s,dp[i,s])  
            return dp[i,s]
        
        ans = helper(0,0)
        return ans if ans != float('inf') else -1