class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if not nums1 or not nums2:
            return 0
        p=len(nums1)+1
        q=len(nums2)+1
        T=[[0]*(q) for _ in range(p)]
        max_=0
        for i in range(p-1):
            for j in range(q-1):
                if nums1[i]==nums2[j]:
                    T[i][j]=T[i-1][j-1]+1
                else:
                    T[i][j]=0
                max_=max(T[i][j],max_)
        
        return max_