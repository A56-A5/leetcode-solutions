class Solution(object):
    def reverse(self, x):
        a=" "
        y=False
        x = str(x)
        for i in x:
            if i!="-":
                a+=i
            if i=="-":
                y=True
        if y:
            a+="-"
        a = int(a[::-1]) 
        if a> 2147483647 or a<-2147483648:
            return 0
        else:
            return a
             