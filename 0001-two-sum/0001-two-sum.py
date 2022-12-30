class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen=collections.defaultdict(int)
        for i,val in enumerate(nums):
            if target-val not in seen:
                seen[val]=i
            else:
                return seen[target-val],i
    