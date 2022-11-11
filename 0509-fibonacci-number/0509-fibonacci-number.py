class Solution:
    def fib(self, n: int) -> int:
        if n<2:
            return n
        T=[0]*n
        T[0]=1
        T[1]=1
        for i in range(2,n):
            T[i]=T[i-1]+T[i-2]
        # print(T)
        return T[-1]