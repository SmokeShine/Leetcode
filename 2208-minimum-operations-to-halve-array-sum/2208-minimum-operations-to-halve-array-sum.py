class Solution:
    def halveArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        val=sum(nums)
        expected=val/2
        heap=[-x for x in nums]
        count=0
        heapq.heapify(heap)
        while val>expected:
            count+=1
            x=heapq.heappop(heap)
            val=val+x/2
            heapq.heappush(heap,x/2)
            
        return count
        