class Solution:
    # def encode(self, strs: List[str]) -> str:
    #     if len(strs) > 0:
    #         result = strs[0]
    #     else:
    #         return "NULL"
    #     for i in range(1, len(strs)):
    #         result += "#"
    #         result += strs[i]
    #     return result
    # def decode(self, s: str) -> List[str]:
    #     if s == "NULL":
    #         return []
    #     else:
    #         return s.split("#")
    def encode(self, strs: List[str]) -> str:
        if not strs or len(strs) == 0:
            return ""

        res = []
        for string in strs:
            res.append(str(len(string)))
            res.append("#")
            res.append(string)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        if not s or len(s) == 0:
            return []

        res = []
        left, right = 0, 0
        while right < len(s):
            while s[right] != "#":
                right += 1

            curr_len = int(s[left:right])
            left = right + 1
            right = left + curr_len
            res.append(s[left:right])

            left = right

        return res