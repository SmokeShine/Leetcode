class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        a1=defaultdict(int)
        a2=defaultdict(int)
        for (i,j) in matches:
            a1[i]=a1[i]+1
            a2[j]=a2[j]+1
        answer=[]
        x=[]
        for i in a1:
            if i not in a2:
                x.append(i)
        answer.append(sorted(x))
        y=[]
        for i in a2:
            if a2[i]==1:
                y.append(i)
        answer.append(sorted(y))
        return answer