class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = "".join(filter(str.isalnum, s))
        temp = temp.lower()
        for i in range(len(temp)//2):
            if temp[i] == temp[len(temp)-(1+i)]:
                pass
            else:
                return False
        return True