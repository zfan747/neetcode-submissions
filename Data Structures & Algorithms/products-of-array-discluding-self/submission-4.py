class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i, n in enumerate(nums):
            temp = nums[:]
            if n == 0:
                temp.pop(i)
                result.append(math.prod(temp))
            else:
                temp.pop(i)
                result.append(math.prod(temp))
        return result