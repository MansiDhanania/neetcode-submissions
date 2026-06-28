class Solution:
    def isValid(self, s: str) -> bool:
        a='('
        b=')'
        c='{'
        d='}'
        e='['
        f=']'
        op=[a, c, e]
        cl=[b, d, f]
        temp=""
        if len(s)<=1:
            return False
        else:
            for i in range(len(s)):
                if s[i] in op:
                    temp+=s[i]
                else:
                    if len(temp)==0:
                        return False
                    else:
                        if op[cl.index(s[i])]!=temp[-1]:
                            return False
                        else:
                            temp=temp[:len(temp)-1]
            if len(temp)>=len(s):
                return False
        return len(temp)==0