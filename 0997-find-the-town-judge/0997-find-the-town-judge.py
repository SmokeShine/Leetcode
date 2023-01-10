class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph=collections.defaultdict(set)
        for x,y in trust:
            graph[x].add(y)
            
        ans=[]
        
        for i in range(1,n+1):
            if i not in graph:
                ans.append(i)
        if len(ans)!=1:
            return -1
        
        for i in range(1,n+1):
            if i!=ans[0]:
                if ans[0] not in graph[i]:
                    return -1
                
        return ans[0] 