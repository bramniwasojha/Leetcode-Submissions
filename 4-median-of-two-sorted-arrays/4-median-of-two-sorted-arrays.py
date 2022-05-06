class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        if len(nums1)%2==0:
            return (sorted(nums1)[len(nums1)//2]+sorted(nums1)[(len(nums1)//2)-1])/2
        else:
            return sorted(nums1)[len(nums1)//2]/1