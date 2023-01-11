class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_=[-x for x in nums]
        heapq.heapify(nums_)
        i=0
        while i<k and heapq:
            val=-heapq.heappop(nums_)
            i+=1
            
        return val