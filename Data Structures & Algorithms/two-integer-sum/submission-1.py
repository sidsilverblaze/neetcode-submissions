class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, x in enumerate(nums):
            for idy, y in enumerate(nums):
                if (idx!=idy) & (x+y==target):
                    return [idx,idy]
        