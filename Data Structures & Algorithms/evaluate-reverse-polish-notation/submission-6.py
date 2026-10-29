
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators="+-*/"
        for i in range(len(tokens)):
            if tokens[i] in operators :
                a,b=stack[-2],stack[-1]
                stack.pop()
                stack.pop()
                m=tokens[i]
                if m=="+":
                    stack.append(a+b)
                elif m=="-":
                    stack.append(a-b)
                elif m=="*":
                    stack.append(a*b)
                else :
                    stack.append(int(a/b))

            else:
                stack.append(int(tokens[i]))
        return stack[-1]
        
