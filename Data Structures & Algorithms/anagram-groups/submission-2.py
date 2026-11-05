class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = {}
        res = []

        for s in strs:
            sortedString = "".join(sorted(s))
            if sortedString not in myMap:
                myMap[sortedString] = []
            myMap[sortedString].append(s)

        return list(myMap.values())