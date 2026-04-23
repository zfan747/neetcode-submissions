class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # result = [[strs[0]]]
        # for i in range(1, len(strs)):
        #     temp = True
        #     # print(result)
        #     for j in range(len(result)):
        #         for word in result[j]:
        #             # print(strs[i], word)
        #             # print(len(strs[i]), len(word))
        #             if len(strs[i]) == len(word) and Counter(strs[i]) == Counter(word):
        #                 # print(Counter(strs[i]), Counter(word))
        #                 result[j].append(strs[i])
        #                 temp = False
        #                 break
        #         if not temp:
        #             break
        #     if temp:
        #         result.append([strs[i]])
        # return result

        result = defaultdict(list)

        for str in strs:
            count = [0] * 26

            for c in str:
                count[ord(c) - ord("a")] += 1

            result[tuple(count)].append(str)
        # print(result)
        return list(result.values())




