class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        iter_list = [(num, idx) for idx, num in enumerate(nums)]
        iter_list.sort()
        i,j=0, len(nums)-1
        while i<j:
            curr = iter_list[i][0] + iter_list[j][0]
            if curr==target:
                return [min(iter_list[i][1], iter_list[j][1]), max(iter_list[i][1], iter_list[j][1])]
            elif curr<target:
                i+=1
            else:
                j-=1