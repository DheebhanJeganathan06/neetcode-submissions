class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []

        for num in nums:
            heapq.heappush(maxHeap, -1 * num)

        for i in range (k-1):
            heapq.heappop(maxHeap)

        return -1 * heapq.heappop(maxHeap)