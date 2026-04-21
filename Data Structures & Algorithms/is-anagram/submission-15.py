class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # for i in range(len(s)-1, -1, -1):
        #     if s[i] in t:
        #         t = t.replace(s[i], "", 1)
        #     else:
        #         return False
        # if len(t) == 0:
        #     return True
        # else:
        #     return False
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        # return Counter(s) == Counter(t)