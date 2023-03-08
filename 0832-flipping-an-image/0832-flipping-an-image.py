class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        a=self.reverse_(image)
        return self.flip_(a)
    def flip_(self,lst):
        values=[]
        for i in lst:
            val=[]
            for j in i:
                if j==1:
                    val.append(0)
                else:
                    val.append(1)
            values.append(val)
        return values
    def reverse_(self,lst):
        val=[]
        for i in lst:
            val.append(i[::-1])
        return val