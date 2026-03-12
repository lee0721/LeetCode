class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def _idx(self, ch):
        return ord(ch) - ord('a')

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            i = self._idx(ch)
            if node.links[i] is None:
                node.links[i] = TrieNode()
            node = node.links[i]
        node.end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if node is None: return False

            if i == len(word):
                return node.end

            ch = word[i]
            if ch != '.':
                return dfs(node.links[self._idx(ch)], i + 1)
            for child in node.links:
                if child is not None and dfs(child, i + 1):
                    return True
            return False
        return dfs(self.root, 0)