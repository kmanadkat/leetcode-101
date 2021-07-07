class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) == 0:
            return s

        # Remove trailing spaces and split into array
        sList = s.strip().split(" ")

        # Remove all empty string items
        index = 0
        while index < len(sList):
            if sList[index] == '':
                del sList[index]
            else:
                index += 1

        # Reverse list & join with empty space
        sList = sList[::-1]
        return " ".join(sList)
