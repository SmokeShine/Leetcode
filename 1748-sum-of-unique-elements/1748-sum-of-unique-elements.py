class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dict_=collections.Counter(nums)
        answer=0
        for x,y in dict_.items():
            if y==1:
                answer+=x
        return answer