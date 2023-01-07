class Solution:
    def frequencySort(self, s: str) -> str:
        dict_=collections.Counter(s)
        
        pair=sorted(dict_.items(),key=lambda x:-x[1])
        z=[x*y for x,y in pair]
        return ''.join(z)