class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        pos=-1
        if not word:
            return
        for i,val in enumerate(word):
            if val==ch:
                pos=i
                break
        if pos==-1:
            return word
        s_=word[:pos+1][::-1]+word[pos+1:]
        return s_