class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        if len(triangle)==1:
            return triangle[0][0]
        T=[[math.inf]*(len(triangle)) for _ in range(len(triangle))]
        T[0][0]=triangle[0][0]
        
        for i in range(1,len(triangle)):
            for j in range(i+1):
                if j==0:
                    T[i][j]=T[i-1][j]+triangle[i][j]
                else:
                    T[i][j]=min(T[i-1][j]+triangle[i][j],T[i-1][j-1]+triangle[i][j])
        
        min_=math.inf
        for j in range(len(triangle)):
            min_=min(T[len(triangle)-1][j],min_)
        return min_
                    