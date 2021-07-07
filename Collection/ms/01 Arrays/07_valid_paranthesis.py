class Solution:
    def isValid(self, s: str) -> bool:
        # String should have even length
        if len(s) % 2 != 0:
            return False

        # Use list as Stack DS
        bracStack = []

        # If Bracket open add in Stack else Pop & Check
        for ele in s:
            if ele in ['(', '{', '[']:
                bracStack.append(ele)

            elif ele in [')', '}', ']']:

                # Stack should have atleast 1 opening corresponding to closing bracket
                if len(bracStack) == 0:
                    return False

                topBracStack = bracStack.pop()
                if ele == ')' and topBracStack != '(':
                    return False

                elif ele == '}' and topBracStack != '{':
                    return False

                elif ele == ']' and topBracStack != '[':
                    return False

        # Stack Length Should Be Zero at End
        return True if len(bracStack) == 0 else False
