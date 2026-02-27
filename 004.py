class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        n=len(nums)
        if(n%2!=0):
            return float(nums[n//2])
        else:
            mid1=nums[n//2]
            mid2=nums[n//2-1]
            mid=mid1+mid2
            return mid/2
