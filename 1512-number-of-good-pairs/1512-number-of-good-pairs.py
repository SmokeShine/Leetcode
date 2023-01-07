class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        answer=0
        for i,vali in enumerate(nums):
            for j,valj in enumerate(nums):
                if i<j and nums[i]==nums[j]:
                    answer+=1
        return answer
                    