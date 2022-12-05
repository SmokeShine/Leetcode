class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts=defaultdict(int)
        for i in nums:
            counts[i]+=1
        max_=-math.inf
        for i,j in counts.items():
            if j==1:
                if i>max_:
                    max_=i
        
        return -1 if max_== -math.inf else max_