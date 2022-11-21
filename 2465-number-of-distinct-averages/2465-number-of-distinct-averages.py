class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=sorted(nums)
        answer={}
        for i in range(len(nums)//2):
            diff_=(nums[i]+nums[-i-1])/2
            print(diff_)
            answer[diff_]=answer.get(diff_,0)+1
        print(nums)
        print(answer)
        return len(answer)