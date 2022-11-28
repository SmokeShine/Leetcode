class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix=[nums[0]]
        for i in range(1,len(nums)):
            prefix.append(nums[i]+prefix[-1])
        min_=min(prefix)
        return 1 if min_>=1 else 1-min_