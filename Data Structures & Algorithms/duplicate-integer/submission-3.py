class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = []
        for i in range(len(nums)):
            if nums[i] in temp:
                return True
            else:
                temp.append(nums[i])
        return False