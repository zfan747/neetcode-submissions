import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i, n in enumerate(nums):
            temp = nums[:]
            if n == 0:
                temp.pop(i)
                result.append(int(math.prod(temp)))
            else:

                result.append(int(math.prod(temp)/n))
        return result