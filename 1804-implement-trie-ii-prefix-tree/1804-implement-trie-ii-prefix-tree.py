class TrieNode:
    def __init__(self):
        self.prefix = 0
        self.terminate = 0
        self.d = defaultdict(TrieNode)
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        def add(node,word,i):
            if i == len(word):
                node.prefix+=1
                node.terminate+=1
            else:
                node.prefix +=1
                add(node.d[word[i]],word,i+1)
        add(self.root,word,0)

    def countWordsEqualTo(self, word: str) -> int:
        def search(node,word,i):
            if i == len(word):
                return node.terminate
            else:
                if word[i] not in node.d:
                    return 0
                else:
                    return search(node.d[word[i]],word,i + 1)
        return search(self.root,word,0)

    def countWordsStartingWith(self, prefix: str) -> int:
        def search(node,word,i):
            if i == len(word):
                return node.prefix
            else:
                if word[i] not in node.d:
                    return 0
                else:
                    return search(node.d[word[i]],word,i + 1)
        return search(self.root,prefix,0)

    def erase(self, word: str) -> None:
        def search(node,word,i):
            if i == len(word):
                node.prefix-=1
                node.terminate-=1
                return
            else:
                if word[i] not in node.d:
                    return 
                else:
                    node.prefix-=1
                    search(node.d[word[i]],word,i + 1)
                    return
        return search(self.root,word,0)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)