class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        l = num1.split("+")
        l2 = num2.split("+")
        a = l[0]
        b = l[1]
        c = l2[0]
        d = l2[1]
        a = int(a)
        c = int(c)
        b = int(b[:len(b)-1])
        d = int(d[:len(d)-1])
        real = a * c - b * d
        img = a * d + b * c
        return str(real)+"+"+str(img)+'i'
