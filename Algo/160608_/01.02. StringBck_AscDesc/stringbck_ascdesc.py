# 1. string 거꾸로 나열하기
# 2. 오름차순 / 내림차순
ran_num = [7, 1, 7, 64, 9, 3, 7, 5, 43, 6, 67, 67, 4756, 4567, 32, 2, 5, 2, 6, 54, 4234, 1]
ran_num.sort()
print(ran_num)
print(ran_num[::-1])

for i in range(len(ran_num)):
    print(ran_num[len(ran_num) - i - 1], end=",")

print('')
