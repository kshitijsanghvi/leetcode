class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        sentence = ' '.join(sentence)+" "
        comp = 0
        n = len(sentence)
        for i in range(rows):
            comp += cols-1
            if sentence[(comp+1) % n] == ' ':
                comp+=1
            else:
                while sentence[(comp) % n] != ' ':
                    comp-=1
            comp+=1
        return (comp+1)//n
                
                