class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return 0
        if numRows==1:
            return [[1]]
        T=[[0]*numRows for _ in range(numRows)]
        for i in range(numRows):
            T[0][i]=1
            T[i][0]=1
        for i in range(1,numRows):
            for j in range(numRows-i):
                T[i][j]=T[i-1][j]+T[i][j-1]
        
        import numpy as np
        matrix = np.array(T)
        
        diags = [np.rot90(matrix[:i,:i]).diagonal().tolist() for i in range(numRows+1)]
        
                
        return [x for x in diags if x]