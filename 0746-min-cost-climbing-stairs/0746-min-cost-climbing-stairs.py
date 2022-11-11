class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        
        # if len(cost)<=2:
        #     return 0
        T=[0]*(len(cost)+1)
        T[0]=0
        T[1]=0
        T[2]=min(cost[0],cost[1])
        # print(T)
        for i in range(3,len(T)):
            T[i]=min(T[i-1]+cost[i-1],T[i-2]+cost[i-2])
            
        return T[-1]