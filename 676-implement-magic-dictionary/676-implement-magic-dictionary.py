class MagicDictionary:

    def __init__(self):
        self.d = defaultdict(list)
    
    def buildDict(self, dictionary: List[str]) -> None:
        
        for w in dictionary:
            
            nw = len(w)
            for i in range(nw):
                self.d[w[:i]+'*'+w[i+1:]].append(w[i])

    def search(self, searchWord: str) -> bool:
        w = searchWord
        nw = len(w)
        for i in range(nw):
            if w[:i]+'*'+w[i+1:] in self.d:
                
                if w[i] in self.d[w[:i]+'*'+w[i+1:]] and len(self.d[w[:i]+'*'+w[i+1:]]) == 1:
                    continue
                
                else:
                    return True
            
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)