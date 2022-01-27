class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        return sum([v*(v+1)//2 for v in Counter(s).values()])