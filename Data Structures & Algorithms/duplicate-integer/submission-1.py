class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for i, num in enumerate(nums):
            if seen.get(num):
                return True
            seen[num] = 1
        return False