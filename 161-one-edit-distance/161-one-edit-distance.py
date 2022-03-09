class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        
        n_s = len(s)
        n_t = len(t)
        
        i_s = 0
        i_t = 0
        
        while i_s < n_s and i_t < n_t:
            if s[i_s] != t[i_t]:
                #insertion
                op1 = s[i_s:] == t[i_t+1:]
                #deletion
                op2 = s[i_s+1:] == t[i_t:]
                #replace
                op3 =  s[i_s+1:] == t[i_t+1:]
                return op1 or op2 or op3
            i_s += 1
            i_t += 1
        if abs(n_t - n_s) == 1:
            return True
        return False
        