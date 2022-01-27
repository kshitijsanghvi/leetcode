class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        c = Counter(s)
        return sum([v*(v+1)//2 for v in c.values()])