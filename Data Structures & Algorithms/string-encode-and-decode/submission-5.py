class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) > 0:
            result = strs[0]
        else:
            return "None"
        for i in range(1, len(strs)):
            print("buh")
            result += "`"
            result += strs[i]
        return result
    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        else:
            return s.split("`")