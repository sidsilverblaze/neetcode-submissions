class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        #print(nums)
        n = len(nums)
        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i]==nums[i-1]:
                continue
            target = -nums[i]
            j = i+1
            k=n-1
            while(j<k):
                total = nums[j] + nums[k]
                if total==target:
                    answer.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
                    #break
                elif total > target:
                    k-=1
                else:
                    j+=1
        return answer
        