class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def compute_prefix(s1,s2):
            i = 0
            while i < min(len(s1),len(s2)):
                if s1[i] != s2[i]:
                    break
                else:
                    i += 1
            return s1[:i]
        
        prefix = strs[0]
        for i in range(1,len(strs)):
            prefix = compute_prefix(prefix,strs[i])
        return prefix
                