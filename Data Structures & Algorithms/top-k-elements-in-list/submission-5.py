class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # my_dict = {}

        # for n in nums:
        #     if n in my_dict:
        #         my_dict[n] += 1
        #     else:
        #         my_dict[n] = 1
        # # print(my_dict)
        # sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
        # # print(sorted_dict)
        # result = []

        # for key in sorted_dict:
        #     if k > 0 :
        #         result.append(key)
        #         k -= 1

        # return result

        result = dict(Counter(nums))
        sorted_result = sorted(result, key = lambda x: result[x], reverse=True)
        print(sorted_result)
        return sorted_result[:k]




