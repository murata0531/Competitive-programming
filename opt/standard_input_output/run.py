#コード実行用領域

N = int(input())
list_x = []
list_y = []
for i in range(N):
    x, y = map(int,input().split())
    list_x.append(x)
    list_y.append(y)
print(list_x)
print(list_y)