class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if not roads:
            return 0
        graph=collections.defaultdict(list)
        for x,y in roads:
            graph[x].append(y)
            graph[y].append(x)
        max_=-math.inf
        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                count=len(graph[i])+len(graph[j])
                if i in graph[j]:
                    count-=1
                max_=max(max_,count)
        return max_
            