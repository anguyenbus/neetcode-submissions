import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # main work here: let the new number into the room
        heapq.heappush(self.heap, val)

        # too many people? kick out the smallest
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # answer: the smallest of the top-k is the kth largest
        return self.heap[0]
