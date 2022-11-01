class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return 
        temp=[0]*len(nums)
        k=k%len(nums)
        if k==0:
            return
        
        j=0
        for i in range(k,len(nums)):
            temp[i]=nums[j]
            j+=1
        
        for i in range(k):
            temp[i]=nums[len(nums)-k+i]
            
        nums[:]=temp[:]