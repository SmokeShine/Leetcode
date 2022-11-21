class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        
        T=[[1]*(i+1) for i in range(rowIndex+1)]
        
        for i in range(rowIndex+1):
            for j in range(1,i):
                T[i][j]=T[i-1][j-1]+T[i-1][j]
        
        return T[-1]