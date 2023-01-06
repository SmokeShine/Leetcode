class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        base=[0]
        base.extend(nums)
        base.append(0)
        nums=base
        cumsum=[0]*len(nums)
        
        for i in range(len(nums)):
            cumsum[i]=cumsum[i-1]+nums[i]
         
        answer=-1
        for i in range(1,len(nums)-1):
            prev=cumsum[i-1]
            curr=nums[i]
            next_=cumsum[-1]-cumsum[i+1]+nums[i+1]
            if prev==next_:
                return i-1
                
        return answer