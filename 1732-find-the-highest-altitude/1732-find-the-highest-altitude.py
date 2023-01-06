class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        if not gain:
            return 0
        cumsum=[0]*(len(gain))
        cumsum[0]=gain[0]
        for i in range(1,len(gain)):
            cumsum[i]=cumsum[i-1]+gain[i]
        return max(max(cumsum),0)