class Solution:
    def hammingWeight(self, n: int) -> int:
        n_=str(bin(n))
        return sum(1 for x in n_ if x=='1')