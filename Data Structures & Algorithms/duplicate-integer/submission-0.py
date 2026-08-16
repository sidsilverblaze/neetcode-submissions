class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_message_set = set(nums)
        return len(nums)!=len(unique_message_set)
