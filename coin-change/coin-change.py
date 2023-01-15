class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        rows=len(coins)
        import math
        T=[[math.inf]*(amount+1) for _ in range(rows+1)]
        
        for i in range(rows+1):
            T[i][0]=0
            
        for i in range(1,rows+1):            
            for j in range(1,amount+1):            
                min_=T[i-1][j]
                if j>=coins[i-1]:
                    min_=min(T[i][j-coins[i-1]]+1,min_)
                
                T[i][j]=min_
                
        
        return T[-1][-1] if T[-1][-1]!=math.inf else -1 