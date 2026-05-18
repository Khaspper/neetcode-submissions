class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        closing = {')', ']', '}'}

        for p in s:
            if p in closing:
                if myStack and ((myStack[-1] == '(' and p == ')') or 
                (myStack[-1] == '[' and p == ']') or 
                (myStack[-1] == '{' and p == '}')):
                    myStack.pop()
                else:
                    return False
            else:
                myStack.append(p)

        if myStack:
            return False

        return True