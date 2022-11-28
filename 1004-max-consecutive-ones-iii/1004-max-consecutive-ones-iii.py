class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        ans=0
        curr=0
        
        left=0
        for right in range(len(nums)):
            if nums[right]==0:
                curr+=1
            
            while curr>k:
                if nums[left]==0:
                    curr-=1
                left+=1
                
            ans=max(ans,right-left+1)
            # print(curr,ans)
                
        return ans
            