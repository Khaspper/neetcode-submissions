class MedianFinder:

    def __init__(self):
        self.smallHeap, self.largeHeap = [], []


    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallHeap, num * -1)
        if (self.smallHeap and self.largeHeap) and self.smallHeap[0] * -1 > self.largeHeap[0]:
            heapq.heappush(self.largeHeap, heapq.heappop(self.smallHeap) * -1)

        if len(self.smallHeap) > len(self.largeHeap) + 1:
            heapq.heappush(self.largeHeap, heapq.heappop(self.smallHeap) * -1)

        if len(self.smallHeap) + 1 < len(self.largeHeap):
            heapq.heappush(self.smallHeap, heapq.heappop(self.largeHeap)  * -1)
        

    def findMedian(self) -> float:
        if len(self.smallHeap) > len(self.largeHeap):
            return self.smallHeap[0] * -1
        if len(self.smallHeap) < len(self.largeHeap):
            return self.largeHeap[0]
        return ((self.smallHeap[0] * -1) + self.largeHeap[0]) / 2
        
        