# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if not n:
            return False
        return self.binarysearch(n,1,n)
    def binarysearch(self,n,start,end):
        if start==end:
            if isBadVersion(start):
                return start
        if end-start==1:
            if isBadVersion(start):
                return start
            else:
                return end
        mid=start + ((end-start) //2)
        if isBadVersion(mid):
            return self.binarysearch(n,start,mid)
        else:
            return self.binarysearch(n,mid,n)