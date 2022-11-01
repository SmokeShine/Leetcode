class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not nums:
            return None
        return self.mergesort(nums,0,len(nums)-1)
    def mergesort(self,nums,start,end):
        if start==end:
            return [nums[start]**2]
        mid=start + ((end-start)//2)
        left= self.mergesort(nums,start,mid)
        right=self.mergesort(nums,mid+1,end)
        return self.merge(left,right)
    def merge(self,left,right):
        i=0
        j=0
        temp_=[0]*(len(left)+len(right))
        for n in range(len(temp_)):
            if j<len(right) and i<len(left):
                if left[i]<right[j] :
                    temp_[n]= left[i]
                    i+=1
                else:
                    temp_[n]= right[j]
                    j+=1
            elif i<len(left) :
                temp_[n]= left[i]
                i+=1
            else:
                temp_[n]= right[j]
                j+=1
                
        return temp_