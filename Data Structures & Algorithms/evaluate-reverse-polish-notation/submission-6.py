class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op=['+', '-', '*', '/']
        temp=[]
        for i in range(len(tokens)):
            if tokens[i]=='+':
                p=temp.pop()
                q=temp.pop()
                ans=p+q
                temp.append(ans)
            elif tokens[i]=='-':
                p=temp.pop()
                q=temp.pop()
                ans=q-p
                temp.append(ans)
            elif tokens[i]=='*':
                p=temp.pop()
                q=temp.pop()
                ans=p*q
                temp.append(ans)
            elif tokens[i]=='/':
                p=temp.pop()
                q=temp.pop()
                ans=int(q/p)
                temp.append(ans)
            else:
                temp.append(int(tokens[i]))
        return int(temp[0])