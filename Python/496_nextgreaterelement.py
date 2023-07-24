class Solution:
    def check(self, number, nums1, nums2):
        index = nums2.index(number)
        return next(
            (nums2[_] for _ in range(index, len(nums2)) if (nums2[_] > number)), -1
        )

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [self.check(x, nums1, nums2) for x in nums1]
