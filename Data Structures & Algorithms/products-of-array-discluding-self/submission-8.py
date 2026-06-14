class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        # for i, n in enumerate(nums):
        #     temp = nums[:]
        #     if n == 0:
        #         temp.pop(i)
        #         result.append(math.prod(temp))
        #     else:
        #         temp.pop(i)
        #         result.append(math.prod(temp))

        for i in range(len(nums)):
            result.append(math.prod(nums[:i]) * math.prod(nums[i+1:]))
        return result