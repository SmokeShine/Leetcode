class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen=[False]*n
        stack=[]
        count=0
        graph=collections.defaultdict(list)
        for x in edges:
            p,q=x
            graph[p].append(q)
            graph[q].append(p)
            
        for i in range(n):
            if not seen[i]:
                seen[i]=True
                count+=1
                stack.append(i)
                while stack:
                    node=stack.pop()
                    for neighbours in graph[node]:
                        if not seen[neighbours]:
                            seen[neighbours]=True
                            stack.append(neighbours)
        return count
                    