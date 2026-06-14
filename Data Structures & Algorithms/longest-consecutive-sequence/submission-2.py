class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        if len(nums) == 0:
            return 0
        result = 1
        temp = 1
        count = nums[0]
        for i in range(1, len(nums)):
            if count == nums[i]:
                continue
            count += 1
            if count == nums[i]: 
                temp += 1
                continue
            
            if temp > result:
                result = temp
            temp = 1
            count = nums[i]
            
        if temp > result:
                result = temp

        return result