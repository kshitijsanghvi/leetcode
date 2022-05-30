class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_count_of_signature = defaultdict(int)
        
        def compute_signature(word):
            s = 0
            for ch in word:
                s = s | 1<<(ord(ch)-ord('a'))
            return s
        
        for word in words:
            s = compute_signature(word)
            max_count_of_signature[s] = max(max_count_of_signature[s], len(word))
            
        keys = list(max_count_of_signature.keys())
        n = len(keys)
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                if keys[i] & keys[j] == 0:
                    ans = max(ans,max_count_of_signature[keys[i]] * max_count_of_signature[keys[j]] )
        return ans
        
        
            
                
            
            