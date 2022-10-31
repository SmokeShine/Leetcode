class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        return self.binarysearch(nums,0,len(nums)-1,target)
    
    def binarysearch(self,nums,start,end,target):
        if start==end:
            if nums[start]==target:
                return start
            else:
                return -1
        mid=start + ((end-start)//2)
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            return self.binarysearch(nums,start,mid,target)
        elif nums[mid]<target:
            return self.binarysearch(nums,mid+1,end,target)
                
        
        