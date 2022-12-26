class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        num_cities=len(isConnected)
        seen=set()
        count=0
        stack=[]
        
        for i in range(num_cities):
            if i not in seen:
                stack.append(i)
                while stack:
                    node=stack.pop()
                    if node not in seen:
                        seen.add(node)
                        for j in range(num_cities):
                            if isConnected[node][j]==1:
                                stack.append(j)
                count+=1
                
            
        return count
                        
                