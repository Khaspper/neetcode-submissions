class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minHeap, maxHeap = [], []
        total = w

        for i in range(len(profits)):
            pair = (capital[i], profits[i])
            heapq.heappush(minHeap, pair)
        print(minHeap)

        while k > 0:
            while minHeap and minHeap[0][0] <= total:
                capital, profit = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, (profit * -1, capital))
            if maxHeap:
                total += heapq.heappop(maxHeap)[0] * -1
                k -= 1
        return total