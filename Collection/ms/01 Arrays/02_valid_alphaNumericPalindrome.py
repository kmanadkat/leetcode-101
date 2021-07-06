class Solution:
    def checkRange(self, x):
        if (x.lower() >= 'a' and x.lower() <= 'z') or (x.lower() >= '0' and x.lower() <= '9'):
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        # Make everything Lower & Filter non-alphaNumeric
        alphaNumericStr = [x.lower() for x in s if self.checkRange(x)]

        return alphaNumericStr == alphaNumericStr[::-1]
