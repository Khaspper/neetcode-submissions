class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = []
        res = 0
        myMap = {}
        maxNumber = 0

        for h in heights:
            maxNumber = max(maxNumber, h)
            if h not in myMap:
                myMap[h] = 0
            myMap[h] += 1

        for n in range(1, maxNumber + 1, 1):
            if n not in myMap:
                continue
            expected = expected + [n for _ in range(myMap[n])]
            del myMap[n]

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1

        return res