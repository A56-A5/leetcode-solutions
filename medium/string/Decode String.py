class Solution(object):
    def decodeString(self, s):
        r=""
        n=0
        x=list()
        for i in s:
            if i=='[':
                x.append(r)
                x.append(n)
                r=""
                n=0
            elif i==']':
                tn = x.pop()
                tr = x.pop()
                r = tr+tn*r
            elif i.isdigit():
                n = n*10+int(i)
            else:
                r+=i
        return r
        