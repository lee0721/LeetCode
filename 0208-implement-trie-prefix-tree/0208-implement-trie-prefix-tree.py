class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.end = False

    def contains_key(self, ch: str) -> bool:
        return self.links[ord(ch) - ord('a')] is not None

    def get(self, ch: str):
        return self.links[ord(ch) - ord('a')]

    def put(self, ch: str, node) -> None:
        self.links[ord(ch) - ord('a')] = node

    def set_end(self) -> None:
        self.end = True


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            if not node.contains_key(ch):
                node.put(ch, TrieNode())
            node = node.get(ch)

        node.set_end()

    def _search_prefix(self, s: str):
        node = self.root

        for ch in s:
            if not node.contains_key(ch):
                return None
            node = node.get(ch)

        return node

    def search(self, word: str) -> bool:
        node = self._search_prefix(word)
        return node is not None and node.end

    def startsWith(self, prefix: str) -> bool:
        return self._search_prefix(prefix) is not None
