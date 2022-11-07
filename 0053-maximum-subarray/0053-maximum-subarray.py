class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        T=[0]*len(nums)
        T[0]=nums[0]
        for i in range(1,len(nums)):
            T[i]=max(nums[i],T[i-1]+nums[i])
        print(T)
        return max(T)