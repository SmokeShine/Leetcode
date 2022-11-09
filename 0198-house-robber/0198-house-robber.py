class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n=len(nums)
        if n<=2:
            return max(nums)
        T=[0]*len(nums)
        T[0]=nums[0]
        T[1]=max(nums[0],nums[1])
        
        for i in range(2,n):
            T[i]=max(T[i-2]+nums[i],T[i-1])
        
        return max(T)
            