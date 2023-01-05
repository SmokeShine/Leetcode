class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        min_=math.inf
        left=0
        sum_=0
        for right in range(len(nums)):
            sum_+=nums[right]
            while sum_>=target:
                min_=min(min_,right-left+1)
                sum_-=nums[left]
                left+=1
                
        return min_ if min_!=math.inf else 0
            