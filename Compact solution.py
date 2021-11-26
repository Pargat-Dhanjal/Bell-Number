import math
b=lambda n: 1 if n<1 else sum([math.comb(n-1,k)*b(k) for k in range(0,n)])
print(b(5))
#Reference https://en.wikipedia.org/wiki/Bell_number#cite_ref-FOOTNOTEWilf199423_8-0
