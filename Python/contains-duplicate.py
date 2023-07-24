# Autor: Anuj Sharma (@optider)
# Github Profile: https://github.com/Optider/
# Problem Link: https://leetcode.com/problems/contains-duplicate/


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for n in nums:
            if count.get(n) is None:
                count[n] = 1
            else:
                return True
        return False
