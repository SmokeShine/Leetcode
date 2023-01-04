class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return
        words=s.split()
        answer=[]
        for word in words:
            answer.append(self.reverse_([x for x in word]))
        return ' '.join(answer)
    def reverse_(self,word):
        if not word:
            return
        i=0
        j=len(word)-1
        while i<j:
            word[i],word[j]=word[j],word[i]
            i+=1
            j-=1
        return ''.join(word)
            
        