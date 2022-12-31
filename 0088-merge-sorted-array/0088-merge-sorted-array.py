class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return nums1
        if not nums1:
            return []
        
        i=0
        j=0
        answer=[]
        while i<m and j<n:
            if nums1[i]>nums2[j]:
                answer.append(nums2[j])
                j+=1
            else:
                answer.append(nums1[i])
                i+=1
        while i<m:
            answer.append(nums1[i])
            i+=1
        while j<n:
            answer.append(nums2[j])
            j+=1
        for i in range(m+n):
            nums1[i]=answer[i]
            
        
            
                                                                                                                                                                                                                                                                                                                                                      