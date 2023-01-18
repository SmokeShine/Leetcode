class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict_=collections.defaultdict(int)
        for i in nums:
            if i in nums:
                dict_[i]=dict_.get(i,0)+1
            else:
                dict_[i]=1
        for x,y in dict_.items():
            if y==1:
                return x