#約数の和を求める
n = 1
x = 1234567890
ans = 0
while n <= 5000000:
    if x % n == 0:
        ans += n
    n  +=  1
print(ans)