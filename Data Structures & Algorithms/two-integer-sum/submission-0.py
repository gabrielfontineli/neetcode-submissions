class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        response = {}
        for i, i_value in enumerate(nums) :
            for j, j_value in enumerate(nums):
                if i != j and j_value + i_value == target:
                    return [min(i, j), max(i, j)]