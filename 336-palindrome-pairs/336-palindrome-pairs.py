class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_pal(s):
            return s == s[::-1]
        
        
        def valid_prefix(s):
            for i in range(len(s)):
                if is_pal(s[i:]):
                    yield s[:i]
        
        def valid_suffix(s):    
            for i in range(len(s)+1):
                if is_pal(s[:i]):
                    yield s[i:]
        
        d = {w:i for i,w in enumerate(words)}
        ans = []
        for i,word in enumerate(words):
            rev = words[::-1] 

            for prefix in valid_prefix(word):
                rev = prefix[::-1]
                
                if  rev in d:
                    if i != d[rev]:
                        ans.append([i,d[rev]])
                
            for suffix in valid_suffix(word):
                rev = suffix[::-1]
                
                if  rev in d:
                    if i != d[rev]:
                        ans.append([d[rev],i])
        return ans
                