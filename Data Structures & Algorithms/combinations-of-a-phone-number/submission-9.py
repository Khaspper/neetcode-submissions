class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        self.myMap = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }

        res = []

        def dfs(curr, digits):
            if len(digits) == 0:
                res.append(curr)
                return
            letters = self.myMap[digits[0]]
            for l in letters:
                dfs(curr + l, digits[1:])

        dfs("", digits)

        return res