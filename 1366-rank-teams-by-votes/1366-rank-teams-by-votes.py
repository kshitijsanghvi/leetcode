class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        dp = defaultdict(int)
        number_of_teams = len(votes[0])
        number_of_people = len(votes)
        teams = list(votes[0])   
        for v in votes:
            for i,c in enumerate(v):
                dp[c,i]+=1
        h = []
        
        for i in teams:
            a = [ -dp[i,j] for j in range(number_of_teams)]
            a.append(i)
            heapq.heappush(h,a)
        
        ans = ""
        while h:
            ans+= heapq.heappop(h)[-1]    
        
        return ans