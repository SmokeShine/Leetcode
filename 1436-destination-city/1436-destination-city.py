class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        graph=collections.defaultdict(list)
        cities=set()
        for x,y in paths:
            if x not in cities:
                cities.add(x)
            if y not in cities:
                cities.add(y)
            graph[x].append(y)
            
        
        for x in cities:
            if x not in graph:
                return x
            
            
            