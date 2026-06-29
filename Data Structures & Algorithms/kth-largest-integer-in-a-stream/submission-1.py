class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappop(self.minHeap)
        heapq.heappush(self.minHeap, val)
        return self.minHeap[0] 
        
