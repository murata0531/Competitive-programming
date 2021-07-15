import sys

#2つの数字だけ標準入力を行う
a,b=map(int,input().split())

print(a)

#入力回数を決める
N=int(input())

#内包表記で数値を入れる
a,b,c=[int(input()) for i in range(N)]
print(a,b,c)

#普通のfor文で数値を入れる
list=[]
for i in range(N):
    list.append(int(input()))

print(list)

#複数行を配列にまとめる

number = int(input())
result = 0
for i in range(number):
    line = input()
    array = line.split()
    # 試しに足し込んでみましょう
    result += int(array[0] + int(array[1]))

print(result)