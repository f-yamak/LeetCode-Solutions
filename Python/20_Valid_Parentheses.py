class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        else:
            counter = 0
            stack = []
            while(counter < len(s)):
                if s[counter] == "(" or s[counter] == "[" or s[counter] == "{":
                    stack.append(s[counter])
                    counter +=1
                else:
                    if not stack:
                        return False
                    elif (stack[-1] == '(') and (s[counter] == ')'):
                        stack.pop()
                        counter +=1
                    elif (stack[-1] == '[') and (s[counter] == ']'):
                        stack.pop()
                        counter +=1
                    elif (stack[-1] == '{') and (s[counter] == '}'):
                        stack.pop()
                        counter +=1
                    else:
                        return False
            return len(stack) == 0    