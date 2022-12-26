class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        if not edges:
            return 0
        if 0 in restricted:
            return 0
        R_=set(restricted)
        stack=[]
        graph=collections.defaultdict(list)
        for x in edges:
            p,q=x
            graph[p].append(q)
            graph[q].append(p)
            
        
                
        seen=[False]*n
        
        seen[0]=True
        stack.append(0)
        count=1
        while stack:
            node=stack.pop()
            for neighbours in graph[node]:
                if not seen[neighbours]:
                    seen[neighbours]=True
                    if neighbours not in R_:
                        stack.append(neighbours)
                        count+=1
                
        return count