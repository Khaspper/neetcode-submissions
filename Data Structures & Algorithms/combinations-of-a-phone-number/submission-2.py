class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        myMap = {'2': ['a', 'b', 'c'], '3': ['d','e','f'], '4': ['g','h','i'],
                 '5': ['j','k','l'], '6': ['m','n','o'], '7': ['p','q','r','s'], 
                 '8': ['t','u','v'], '9':['w','x','y','z']}
        res = []
        def dfs(level, curr):
            if len(curr) == len(digits):
                res.append(''.join(curr))
                return
            for j in range(len(myMap[digits[level]])):
                curr.append(myMap[digits[level]][j])
                dfs(level + 1, curr)
                curr.pop()
        dfs(0,[])
        return res