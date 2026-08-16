class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        n=len(nums)
        x=1
        for i in range(0,n):
            output[i] = x
            x*=nums[i]
        x=1
        for i in range(n-1,-1,-1):
            output[i]*=x
            x*=nums[i]
        return output
