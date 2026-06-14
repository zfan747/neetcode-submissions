class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # result = []
        # for i, n in enumerate(nums):
        #     # temp = nums[:]
        #     temp = nums.copy()
        #     if n == 0:
        #         temp.pop(i)
        #         result.append(math.prod(temp))
        #     else:
        #         temp.pop(i)
        #         result.append(math.prod(temp))
        # for i in range(len(nums)):
        #     result.append(math.prod(nums[:i]) * math.prod(nums[i+1:]))
        
        n = len(nums)
        result = [1] * n
        
        # First pass: store prefix products in result
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        
        # Second pass: multiply by suffix products
        suffix = 1
        for i in range(n-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        return result