class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0
        for i in nums:
            if i - 1 not in num_set:
                length=0
                while i + length in num_set:
                    length+=1
                max_length = max(max_length, length)
        return max_length
        