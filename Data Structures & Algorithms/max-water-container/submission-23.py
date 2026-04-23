class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # largest = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         if (min(heights[i], heights[j]) * (j-i)) > largest:
        #             largest = min(heights[i], heights[j]) * (j-i)
        #         else:
        #             pass
        # return largest

        l, r = 0, len(heights) - 1
        result = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            result = max(result, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return result

        # largest = 0
        # max_height = max(heights)
        # # print(max_height)
        # if heights.count(max_height) > 1:
        #     normal_pos = heights.index(max_height)
        #     reverse_pos = heights[::-1].index(max_height)
        #     reverse_pos = len(heights) - reverse_pos - 1
        #     # print(normal_pos, reverse_pos)
        #     best_pos = abs(max(abs(normal_pos - len(heights)), abs(reverse_pos - len(heights))) - len(heights))
        # else:
        #     best_pos = heights.index(max_height)
        # # print(best_pos)
        # # print(heights[best_pos])
        # for i in range(best_pos):
        #     for j in range(i+1, len(heights)):
        #         if (min(heights[i], heights[j]) * (j-i)) > largest:
        #             largest = min(heights[i], heights[j]) * (j-i)
        # # print(largest)
        # for j in range(best_pos + 1, len(heights)):
        #     if (min(heights[best_pos], heights[j]) * abs(j-best_pos)) > largest:
        #         largest = min(heights[best_pos], heights[j]) * abs(j-best_pos)
        # return largest





