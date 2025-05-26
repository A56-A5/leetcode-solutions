class Solution(object):
    def findKthBit(self, n, k):
        def ri(x):
            s = ""
            for i in x:
                if i == "1":
                    s += "0"
                else:
                    s += "1"
            return s[::-1]

        s = ["0"]

        for i in range(1, n):
            s.append(s[i - 1] + "1" + ri(s[i - 1]))

        return s[n - 1][k - 1]
