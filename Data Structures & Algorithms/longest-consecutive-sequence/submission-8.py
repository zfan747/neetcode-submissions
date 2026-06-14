class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        n_s = sorted(set(nums))
        cur_count = 1
        max_count = 1

        for i in range(len(n_s) - 1):
            if n_s[i] + 1 == n_s[i+1]:
                cur_count += 1
            else:
                if cur_count > max_count:
                    max_count = cur_count
                cur_count = 1

        if cur_count > max_count:
            max_count = cur_count

        return max_count