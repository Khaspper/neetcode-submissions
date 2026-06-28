class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        temp = []
        for p in points:
            temp.append((math.sqrt((p[0] - 0)^2 + (p[1] - 0)^2) * -1, p))
        heapq.heapify(temp)

        while len(temp) > k:
            heapq.heappop(temp)

        res = []
        for p in temp:
            res.append(p[1])
        return res