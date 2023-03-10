class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.sort_(nums,0,len(nums)-1)
    def sort_(self,nums,start,end):
        if start==end:
            return [nums[start]]
        mid=start + ((end-start)//2)
        a=self.sort_(nums,start,mid)
        b=self.sort_(nums,mid+1,end)
        return self.mergearray(a,b)
        
    def mergearray(self,a,b):
        c=[0]*(len(a)+len(b))
        i,j=0,0
        for k in range(len(c)):
            if i>len(a)-1:
                c[k]=b[j]
                j+=1
            elif  j>len(b)-1:
                c[k]=a[i]
                i+=1
            elif a[i]<b[j]:
                c[k]=a[i]
                i+=1
            else:
                c[k]=b[j]
                j+=1
        return c