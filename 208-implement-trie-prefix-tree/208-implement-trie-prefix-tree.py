
class TrieNode:
    def __init__(self):
        self.val = False
        self.d = defaultdict(TrieNode)


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        def add(node, word, i):
            if i == len(word):
                node.val = True
            else:
                add(node.d[word[i]], word, i + 1)
        add(self.root,word,0)

    def search(self, word: str) -> bool:
        def ser(node, word, i):
            if i == len(word):
                return node.val
            elif word[i] not in node.d:
                return False
            else:
                return ser(node.d[word[i]], word, i + 1)
        return ser(self.root,word,0)
    def startsWith(self, prefix: str) -> bool:
        def ser(node, word, i):
            if i == len(word):
                return True
            elif word[i] not in node.d:
                return False
            else:
                return ser(node.d[word[i]], word, i + 1)
        return ser(self.root,prefix,0)