class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        myMap = {}

        for first, second in prerequisites:
            if first not in myMap:
                myMap[first] = []
            if second not in myMap:
                myMap[second] = []
            myMap[second].append(first)
        print(myMap)

        def dfs(curr, visited):
            if curr in visited:
                return False
            if myMap[curr] == []:
                return True
            visited.add(curr)
            for n in myMap[curr]:
                if not dfs(n, visited):
                    return False
            visited.remove(curr)
            myMap[curr] = []
            return True

        for i in range(numCourses):
            if i in myMap and not dfs(i, set()):
                return False

        return True