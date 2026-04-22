class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        temp = []
        start = ['(', '[', '{']
        complete = ['()', '[]', "{}"]
        for i in range(len(s)):
            if s[i] in start:
                temp.append(s[i])
            else:
                try:
                    if temp[-1] + s[i] in complete:
                        temp.pop(-1)
                    else:
                        return False
                except:
                    return False
        if len(temp) != 0:
            return False
        return True