class Solution(object):
    def countPrimes(self, n):
        if n<3: return 0
        lst = [1]*n
        lst[0] = lst[1]= 0
        i = 2
        while i**2 < n:
            if lst[i] == 1:
                lst[i*i:n:i] = [0] * (1+(n-i*i-1)//i)
            i+=1 if i==2 else 2
        return sum(lst)
            