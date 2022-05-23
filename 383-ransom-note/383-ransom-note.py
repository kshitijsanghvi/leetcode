class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn = Counter(ransomNote)
        mag = Counter(magazine)
        
        for i in rn:
            if i not in mag:
                return False
            else:
                if mag[i] < rn[i]:
                    return False
        return True