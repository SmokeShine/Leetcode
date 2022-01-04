class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.pallindrome(word):
                return word
        return ""
    def pallindrome(self, word):
        print(word)
        start=0
        end=len(word)-1
        while start<=end: #this is error area
            if word[start]!=word[end]:
                return False
            start+=1
            end-=1
        return True