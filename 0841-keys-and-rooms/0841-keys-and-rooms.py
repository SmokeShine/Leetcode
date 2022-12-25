class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return False
        num_rooms=len(rooms)
        visited=collections.defaultdict(bool)
        for i in range(num_rooms):
            visited[i]=False
        
        stack=[rooms[0]]
        while stack:
            room=stack.pop()
            print(room)

            for i in room:                
                if visited[i]==False:
                    visited[i]=True
                    stack.append(rooms[i])
        visited[0]=True
        for i in visited:
            if visited[i]==False:
                return False
        return True