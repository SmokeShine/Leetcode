class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        self.maze=maze
        self.entrance=entrance
        queue=collections.deque()
        queue.append(((entrance[0],entrance[1]),0))
        seen=set()
        
        while queue:
            cell,step=queue.popleft()
            
            if cell not in seen:
                seen.add(cell)
            else:
                continue
            if not self.isValid(cell):
                continue
            if self.isExit(cell):
                return step
            
            left=(cell[0],cell[1]-1)
            right=(cell[0],cell[1]+1)
            up=(cell[0]-1,cell[1])
            down=(cell[0]+1,cell[1])
            
            queue.append((left,step+1))
            queue.append((right,step+1))
            queue.append((up,step+1))
            queue.append((down,step+1))
        return -1
    def isValid(self,cell):
        x,y=cell
        if x<0 or x>len(self.maze)-1:
            return False
        if y<0 or y>len(self.maze[0])-1:
            return False
        if self.maze[x][y]=='+':
            return False
        return True
    
    def isExit(self,cell):
        
        x,y=cell
        if x==self.entrance[0] and y==self.entrance[1]:
            return False
        if x==0 or y==0:
            return True
        if x==len(self.maze)-1 or y==len(self.maze[0])-1:
            return True
        
        return False
        