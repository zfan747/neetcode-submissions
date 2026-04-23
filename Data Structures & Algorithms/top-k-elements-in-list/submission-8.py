class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = dict(Counter(nums))
        sorted_result = sorted(result, key = lambda x: result[x], reverse=True)
        # print(sorted_result)
        return sorted_result[:k]




