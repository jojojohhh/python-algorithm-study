import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
p_min = n
p_sum = 0
for i in range(m, n + 1):
    isPrime = True
    if i == 1:
        continue
    for j in range(2, int(i ** 0.5) + 1):  # 에라토스테네스의 접근 (숫자 n은  n의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다.)
        if i % j == 0:
            isPrime = False
            break
    if isPrime or i == 2:
        p_sum += i
        if i < p_min:
            p_min = i
if p_sum == 0:
    print(-1)
else:
    print(p_sum)
    print(p_min)