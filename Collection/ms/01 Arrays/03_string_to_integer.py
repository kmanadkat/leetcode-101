class Solution:
    def sToNum(self, s: str) -> int:
        if len(s) == 0:
            return 0
        num = self.sToNum(s[0:len(s)-1])
        lastDigit = int(s[len(s)-1])

        return num * 10 + lastDigit

    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0

        # Multiplying Factor
        mF = 1

        # Remove whiteSpace
        sTrim = s.strip()

        # Remove letters & check if string has no digits
        si = -1
        ei = 0
        for index, sC in enumerate(sTrim):
            if sC >= '0' and sC <= '9':
                si = index if si == -1 else si
                ei = index
            else:
                if si >= 0 and ei >= 0:
                    break

        # Either start with digit or sign
        if si != 0 and si != 1:
            return 0

        # Zeroth Index Should be in ['-', '+']
        if si == 1 and sTrim[si - 1] not in ['-', '+']:
            return 0

        # Check Leading Sign
        if sTrim[0] == '-':
            mF = -1

        # Use Recursion To Find Number and multiply sign
        sNums = sTrim[si:ei+1]
        ans = self.sToNum(sNums) * mF

        # Check Range
        if ans < -2**31:
            return -2**31
        if ans >= 2**31:
            return 2**31 - 1

        return ans
