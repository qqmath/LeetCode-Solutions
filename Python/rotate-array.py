class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lenz = len(nums)
        k %= lenz
        if k == 0:
            return nums
        nums += nums[:-k]
        del nums[:lenz-k]
        