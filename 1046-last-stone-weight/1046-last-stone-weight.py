class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[-x for x in stones]
        heapq.heapify(heap)
        
        while heap:
            y=-heapq.heappop(heap)
            if not heap:
                return y
            x=-heapq.heappop(heap)
            
            
            if x!=y:
                heapq.heappush(heap,x-y)
        return 0
        