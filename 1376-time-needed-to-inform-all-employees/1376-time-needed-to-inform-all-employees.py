class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        queue=collections.deque()
        graph=collections.defaultdict(list)
        for i in range(n):
            if i!=headID:
                graph[manager[i]].append(i)
        
        queue.append((headID,informTime[headID]))
        total=0
        while queue:
            node,step=queue.popleft()
            total=max(total,step)    
            for neighbours in graph[node]:
                queue.append((neighbours,step+informTime[neighbours]))
        return total        
            
            