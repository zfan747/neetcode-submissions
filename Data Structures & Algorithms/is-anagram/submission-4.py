class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in range(len(s)-1, -1, -1):
            if s[i] in t:
                t = t.replace(s[i], "", 1)
                s = s[:len(s)-1]
            else:
                return False
        if len(s) == 0 and len(t) == 0:
            return True
        else:
            return False