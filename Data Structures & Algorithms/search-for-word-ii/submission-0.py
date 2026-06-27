class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        root = TrieNode()

        for word in words:
            print('adding word: ', word)
            self.addWord(word, root)
        print(root)
        return []
    
    def addWord(self, word: str, root):
        curr = root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]