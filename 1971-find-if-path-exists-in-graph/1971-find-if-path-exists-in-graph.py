class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source==destination:
            return True
        seen=[False]*n
        graph=collections.defaultdict(list)
        stack=[]
        for x in edges:
            p,q=x
            graph[p].append(q)
            graph[q].append(p)
        
            
        seen[source]=True
        stack.append(source)
        while stack:
            node=stack.pop()
            for neighbours in graph[node]:
                if neighbours==destination:
                    return True
                if not seen[neighbours]:
                    seen[neighbours]=True
                    stack.append(neighbours)
        return False