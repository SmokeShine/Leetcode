class Solution:
    def confusingNumber(self, n: int) -> bool:
        conversion=collections.defaultdict(int)
        conversion[0]=0
        conversion[1]=1
        conversion[6]=9
        conversion[8]=8
        conversion[9]=6
        reversed_=0
        n_copy=n
        while n>0:
            i=n%10
            if i not in conversion:
                return False
            
            n=n//10
            reversed_=reversed_*10+conversion[i]
        
        if reversed_==n_copy:
            return False
        return True
        