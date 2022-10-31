class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        return self.binarysearch(nums,0,len(nums)-1,target)
    def binarysearch(self,nums,start,end,target):
        if start==end:
            if nums[start]==target:
                return start
            elif nums[start]<target:
                return start+1
            elif nums[start]>target:
                return start
        if end-start==1:
            if nums[start]==target:
                return start
            elif nums[end]==target:
                return end
            elif nums[end]<target:
                return end+1
            elif nums[start]>target:
                return start
        mid = start + ((end-start)//2)
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            return self.binarysearch(nums,start,mid-1,target)
        else:
            return self.binarysearch(nums,mid+1,end,target)