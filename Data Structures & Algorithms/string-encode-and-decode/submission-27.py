class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) > 0:
            result = strs[0]
        else:
            return "!!"
        for i in range(1, len(strs)):
            result += "!#"
            result += strs[i]
        return result
    def decode(self, s: str) -> List[str]:
        if s == "!!":
            return []
        else:
            return s.split("!#")