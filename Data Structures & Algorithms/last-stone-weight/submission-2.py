class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            firstStone = heapq.heappop(stones) * -1
            secondStone = heapq.heappop(stones) * -1
            diff = abs(firstStone - secondStone)
            if diff != 0:
                heapq.heappush(stones, diff * -1)
        return heapq.heappop(stones) * -1 if len(stones) == 1 else 0