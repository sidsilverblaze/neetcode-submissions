class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prev should start with 1
        # suf should start with n-2
        n=len(nums)
        #prev=suf=nums
        prev=[0] * n
        suf = [0] * n
        prev[0]=suf[n-1]=1
        ans = []

        for i in range(1,n):
            prev[i] = prev[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            suf[i] = suf[i+1]*nums[i+1]
        for i in range(0,n):
            ans.append(prev[i] * suf[i])
        return ans