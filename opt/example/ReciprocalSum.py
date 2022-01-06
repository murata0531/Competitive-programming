#Nまでの逆数和が9を超えるような最小のNを求める
ans = 0
n = 0
while ans < 9:
    n += 1
    ans += 1 / n
    
print(n-1)
print(ans - 1/(n))
print(n)
print(ans)