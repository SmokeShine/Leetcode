class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        length=len(grid)
        breadth=len(grid[0])
        seen=[[False]*breadth for x in range(length)]
        
        stack=[]
        count=0
        for i in range(length):
            for j in range(breadth):
                if not seen[i][j]:
                    seen[i][j]=True
                    if grid[i][j]=="1":
                        count+=1
                        stack.append((i,j))
                        while stack:
                            row,col=stack.pop()
                            if row+1<length and grid[row+1][col]=="1" and not seen[row+1][col]:
                                seen[row+1][col]=True
                                stack.append((row+1,col))
                            if col+1<breadth and grid[row][col+1]=="1" and not seen[row][col+1]:
                                seen[row][col+1]=True
                                stack.append((row,col+1))
                            if row>0 and grid[row-1][col]=="1" and not seen[row-1][col]:
                                seen[row-1][col]=True
                                stack.append((row-1,col))
                            if col>0 and grid[row][col-1]=="1" and not seen[row][col-1]:
                                seen[row][col-1]=True
                                stack.append((row,col-1))
                        
                        
                        
        return count
                            
                        
        