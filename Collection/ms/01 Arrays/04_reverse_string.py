class Solution:
    def reverseString(self, s: List[str]) -> None:
        if len(s) <= 1:
            return
        si = 0
        ei = len(s)-1
        while si < ei:
            s[si], s[ei] = s[ei], s[si]
            si += 1
            ei -= 1
