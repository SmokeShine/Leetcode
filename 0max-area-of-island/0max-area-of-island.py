class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        length=len(grid)
        breadth=len(grid[0])
        
        max_=0
        
        seen=[[False]*breadth for _ in range(length)]
        
        stack=[]
        for i in range(length):
            for j in range(breadth):
                if not seen[i][j]:
                    seen[i][j]=True
                    if grid[i][j]==1:
                        area=1
                        stack.append((i,j))
                        
                        while stack:
                            row,col=stack.pop()
                            
                            
                            if row>0 and grid[row-1][col]==1 and not seen[row-1][col]:
                                stack.append((row-1,col))
                                seen[row-1][col]=True
                                area+=1
                            if col>0 and grid[row][col-1]==1 and not seen[row][col-1]:
                                stack.append((row,col-1))
                                seen[row][col-1]=True
                                area+=1
                            if row+1<length and grid[row+1][col]==1 and not seen[row+1][col]:
                                stack.append((row+1,col))
                                seen[row+1][col]=True
                                area+=1
                            if col+1<breadth and grid[row][col+1]==1 and not seen[row][col+1]:
                                stack.append((row,col+1))
                                seen[row][col+1]=True
                                area+=1
                       
                        
                        max_=max(max_,area)
                        
        return max_
                            
        