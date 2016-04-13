import math

val = input()
val = val.split()

# 짝수의 수
b_even = int(math.sqrt(int(val[1])))
a_even = int(math.sqrt((int(val[0]) - 1)))
even = b_even - a_even

# 홀수의 수
odd = (int(val[1]) - int(val[0]) + 1) - even
print(odd)
