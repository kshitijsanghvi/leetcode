class TrieNode:
    def __init__(self):
        self.val = False
        self.d = defaultdict(TrieNode)
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        
        def add(node,word,i):
            if len(word) == i:
                node.val = True
            else:
                add(node.d[word[i]],word,i+1)

        add(self.root,word,0)
        
    def search(self, word: str) -> bool:
        def search1(node,word,i):
            if i == len(word):
                return node.val
            else:
                if word[i] == '.':
                    return max([0]+[search1(node.d[j],word,i+1) for j in node.d])
                else:
                    if word[i] not in node.d:
                        return False
                    else:
                        return search1(node.d[word[i]],word,i+1)
        return search1(self.root,word,0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)