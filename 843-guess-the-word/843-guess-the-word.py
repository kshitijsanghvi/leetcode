# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:

        def common(s1,s2):
            return sum(1 for i in range(6) if s1[i]==s2[i])
    
            
        for i in range(10):
            g = random.choice(wordlist)
            x = master.guess(g)
            wordlist = [w for w in wordlist if common(w,g) == x]