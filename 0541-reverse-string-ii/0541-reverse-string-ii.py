class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s)<k:
            return self.reverse_([x for x in s])
        answer=[]
        a=-1
        for i in range(0,len(s),k):
            if a<0:
                s_=s[i:i+k]
                curr=self.reverse_([x for x in s_])
            else:
                curr=s[i:i+k]
            answer.append(curr)
            a*=-1
            
        return ''.join(answer)
        
    def reverse_(self,arr):
        i=0
        j=len(arr)-1
        while i<j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
        return ''.join(arr)