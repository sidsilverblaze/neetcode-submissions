class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        nums = list(num_set)
        nums.sort()
        consec_l = []
        max_len=0
        curr_len = 0
        for i in range(len(nums)):
            if len(consec_l)==0:
                consec_l.append(nums[i])
                curr_len+=1
            else:
                if consec_l[-1] + 1==nums[i]:
                    consec_l.append(nums[i])
                    curr_len+=1
                else:
                    consec_l=[nums[i]]
                    curr_len=1
            if max_len<curr_len:
                        max_len+=1
            #print(curr_len)
        return max_len
                
        