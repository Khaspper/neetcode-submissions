class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root
        return self.dfs(curr, word)

    def dfs(self, curr, word):
        if not word:
            return curr.word
        if word[0] != '.' and word[0] not in curr.children:
            return False
        if word[0] == '.':
            for k, v in curr.children.items():
                print(f'k, v: {k}, {v}')
                if self.dfs(v, word[1:]):
                    return True
        if word[0] in curr.children:
            if len(word) == 1:
                print('this is the last word')
                return curr.children[word[0]].word
            return self.dfs(curr.children[word[0]], word[1:])
        return False







