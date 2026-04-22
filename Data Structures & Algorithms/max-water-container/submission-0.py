class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                if (min(heights[i], heights[j]) * (j-i)) > largest:
                    largest = min(heights[i], heights[j]) * (j-i)
                else:
                    pass
        return largest 