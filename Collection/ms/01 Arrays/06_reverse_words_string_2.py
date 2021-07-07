class Solution:

    def revereseStartEnd(self, s: List[str], start: int, end: int) -> None:
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    def reverseWords(self, s: List[str]) -> None:
        if len(s) <= 1:
            return

        # Reverse Whole String
        s.reverse()

        # Iterate & Reverse Each Word
        start = 0
        for i, ele in enumerate(s):
            # Handle Last Word
            if i == len(s) - 1:
                self.revereseStartEnd(s, start, i)
                return

            if ele != ' ':
                i += 1
            else:
                self.revereseStartEnd(s, start, i - 1)
                if i + 1 < len(s):
                    start = i + 1
        return
