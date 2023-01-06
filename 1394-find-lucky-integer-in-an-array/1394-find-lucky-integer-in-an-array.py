class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dict_=collections.Counter(arr)
        answer=-math.inf
        for x,y in dict_.items():
            if x==y:
                answer=max(answer,x)
        return answer if answer!=-math.inf else -1