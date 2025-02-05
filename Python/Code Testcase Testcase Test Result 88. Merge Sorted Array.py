class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        end_x = len(nums1)-1
        for nums in nums2:
                nums1[end_x]=nums
                end_x-=1
        nums1.sort()

        
        
