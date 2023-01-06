class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.cumsum=[0]*len(nums)
        self.cumsum[0]=nums[0]
        for i in range(1,len(nums)):
            self.cumsum[i]=self.cumsum[i-1]+nums[i]
            
            
    def sumRange(self, left: int, right: int) -> int:
        if left==right:
            return self.nums[left]
        return self.cumsum[right]-self.cumsum[left]+self.nums[left]
        #same as initializing nums[left] instead of 0
        #  solve for relation between T(x) and T(x-2) in terms of T(x-3) and nums[x-2]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)