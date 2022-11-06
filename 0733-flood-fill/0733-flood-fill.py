class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return
        self.r=len(image)-1
        self.c=len(image[0])-1
        self.color=color
        self.dict_={}
        target=image[sr][sc]
        if target==color:
            return image
        self.dfs(image,sr,sc,target)
        return image
        
    def dfs(self,image,sr,sc,target):
        if (sr,sc) in self.dict_:
            return
        if sr > self.r or sr < 0:
            self.dict_[(sr,sc)]=1
            return
        if sc > self.c or sc < 0:
            self.dict_[(sr,sc)]=1
            return
        if image[sr][sc]!=target:
            self.dict_[(sr,sc)]=1
            return
        image[sr][sc]=self.color
        #up
        self.dfs(image,sr-1,sc,target)
        self.dict_[(sr-1,sc)]=1
        #down
        self.dfs(image,sr+1,sc,target)
        self.dict_[(sr+1,sc)]=1
        #left
        self.dfs(image,sr,sc-1,target)
        self.dict_[(sr,sc-1)]=1
        #right
        self.dfs(image,sr,sc+1,target)
        self.dict_[(sr,sc+1)]=1
        
        