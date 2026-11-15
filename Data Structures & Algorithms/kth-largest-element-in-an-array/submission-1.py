class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for num in nums:
            # Add current number to min-heap
            heapq.heappush(minHeap, num)

            # Remove smallest number if heap exceeds size k
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        # Smallest element among the k largest is kth largest
        return minHeap[0]
