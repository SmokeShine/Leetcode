class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            if len(curr)==len(nums):
                ans.append(curr[:])
                return
            for i in nums:
                if i not in curr:
                    curr.append(i)
                    backtrack(curr)
                    curr.pop()
        ans=[]
        backtrack([])
        return ans