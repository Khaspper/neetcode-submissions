class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        temp = []
        for p in points:
            x = p[0]
            y = p[1]
            distance = math.sqrt((x - 0)**2 + (y - 0)**2) * -1
            temp.append((distance, p))

        res = []
        heapq.heapify(temp)
        while len(temp) > k:
            heapq.heappop(temp)

        for c in temp:
            res.append(c[1])
        return res