# 標準入力からえた値をソートし最小値、最大値を出力

N = int(input())
min = 0
max = 0

list = [int(e) for e in input().split()]

list.sort()

min = list[0]
max = list[-1]

print('{0} {1}'.format(min,max))

for i in range(len(list)):
    print(list[i], end='')