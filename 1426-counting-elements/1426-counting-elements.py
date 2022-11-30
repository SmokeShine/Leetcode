class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr_set=set(arr)
        ans=0
        for i in arr:
            if i+1 in arr_set:
                ans+=1
        return ans